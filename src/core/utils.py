# -*- coding: utf-8 -*-
import asyncio
import contextlib
import random
import time

import aiohttp
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

__all__ = ['test_ip', 'get_session', 'ip_generator',
           'time_repr', 'read_url', 'read_urls_parallel', 'open_url']

class _TraceContext:
    __slots__ = ('start_time', 'end_time')

    def __init__(self):
        self.start_time = None
        self.end_time = None

    @property
    def duration(self):
        return self.end_time - self.start_time

def _build_trace_timer():
    async def record_start(session, context, params):
        context.trace_request_ctx.start_time = time.perf_counter()

    async def record_end(session, context, params):
        context.trace_request_ctx.end_time = time.perf_counter()

    trace_config = aiohttp.TraceConfig()
    trace_config.on_connection_create_start.append(record_start)
    trace_config.on_request_end.append(record_end)

    return trace_config

async def test_ip(session, ip, host, request_format):
    url = request_format.format(f'[{ip}]' if ':' in ip else ip)
    ctx = _TraceContext()
    try:
        async with session.get(url,
                               server_hostname=host,
                               headers={'Host': host},
                               allow_redirects=False,
                               trace_request_ctx=ctx) as response:
            await response.release()
        return ctx.duration
    except Exception as e:
        return (type(e).__name__, str(e))

def get_session(timeout):
    return aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(
            limit=0,
            use_dns_cache=False,
            force_close=True,
            ssl=True,
            enable_cleanup_closed=True
        ),
        timeout=aiohttp.ClientTimeout(total=timeout),
        cookie_jar=aiohttp.DummyCookieJar(),
        raise_for_status=True,
        trust_env=False,
        auto_decompress=False,
        trace_configs=[_build_trace_timer()]
    )

def ip_generator(networks, shuffle=True):
    if not shuffle:
        for net in networks:
            yield from map(str, net.hosts())
        return

    # <=512 chunks per CIDR, preferred 256 addresses per chunk
    chunks = []
    for net in networks:
        if net.num_addresses <= 256:
            chunks.append(net)
        elif net.num_addresses > 131072:
            chunks.extend(net.subnets(prefixlen_diff=9))
        else:
            chunks.extend(net.subnets(new_prefix=net.max_prefixlen - 8))

    generators = [map(str, chunk.hosts()) for chunk in chunks]
    while generators:
        random.shuffle(generators)
        next_generators = []
        for gen in generators:
            if next_ip := next(gen, None):
                yield next_ip
                next_generators.append(gen)
        generators = next_generators

def time_repr(secs):
    return f'{secs*1000:.0f}ms' if secs < 0.9995 else f'{secs:.2f}s'

def _get_download_session():
    return aiohttp.ClientSession(
        timeout=aiohttp.ClientTimeout(
            total=15,
            connect=3,
            sock_read=3
        ),
        cookie_jar=aiohttp.DummyCookieJar(),
        raise_for_status=True,
        trust_env=True,
        auto_decompress=True,
        headers={'Accept-Encoding': 'gzip, deflate, br'}
    )

async def read_url(url, session=None):
    ctx = contextlib.nullcontext(session) if session else _get_download_session()
    async with ctx as s, s.get(url) as response:
        return set((await response.text()).split())

async def read_urls_parallel(url_groups):
    async def _fetch_group(session, urls):
        tasks = [asyncio.create_task(read_url(url, session)) for url in urls]
        try:
            for coro in asyncio.as_completed(tasks):
                with contextlib.suppress(aiohttp.ClientError, asyncio.TimeoutError):
                    return await coro 
        finally:
            for task in tasks:
                if not task.done():
                    task.cancel()
        return None

    async with _get_download_session() as session:
        results = await asyncio.gather(
            *(_fetch_group(session, urls) for urls in url_groups)
        )
    merged = set()
    failed = []
    for i, result in enumerate(results):
        if result is None:
            failed.append(i)
        else:
            merged |= result
    return merged, failed

def open_url(url):
    QDesktopServices.openUrl(QUrl(url))
