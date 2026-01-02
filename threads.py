# -*- coding: utf-8 -*-
import asyncio
from PySide6.QtCore import QThread, Signal
from utils import get_session, ip_generator, test_ip

__all__ = ['SpeedtestThread', 'ScanThread', 'DebugThread']


class SpeedtestThread(QThread):
    foundAvailable = Signal(str, float)  # (ip, latency)
    foundUnavailable = Signal(str, str)  # (ip, reason)

    def __init__(self, parent, ips, host, request_format,
                 timeout=2.5, repeat=3, num_workers=8):
        super().__init__(parent)
        self.ips = ips
        self.host = host
        self.request_format = request_format
        self.timeout = timeout
        self.repeat = repeat
        self.num_workers = num_workers

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(self._run_async())
        finally:
            loop.close()

    async def _test_one(self, sem, session, ip):
        async with sem:
            total = 0.0
            for _ in range(self.repeat):
                result = await test_ip(session, ip, self.host, self.request_format)
                if isinstance(result, tuple):
                    self.foundUnavailable.emit(ip, result[0])
                    return
                total += result
                await asyncio.sleep(0.1)
            latency = total / self.repeat
            self.foundAvailable.emit(ip, latency)

    async def _run_async(self):
        sem = asyncio.Semaphore(self.num_workers)
        async with get_session(self.timeout) as session:
            tasks = []
            warmup_left = self.num_workers
            warmup_delay = 2 * self.timeout / self.num_workers
            for ip in self.ips:
                tasks.append(asyncio.create_task(self._test_one(sem, session, ip)))
                if warmup_left > 0:
                    await asyncio.sleep(warmup_delay)
                    warmup_left -= 1
            await asyncio.gather(*tasks)


class ScanThread(QThread):
    foundAvailable = Signal(str, float)
    progressUpdate = Signal(int)

    def __init__(self, parent, ip_networks, host, request_format,
                 max_ips=5, num_workers=80, timeout=2.5, randomized=False):
        super().__init__(parent)

        self.networks = ip_networks
        self.total_ips = sum(net.num_addresses for net in ip_networks)
        self.host = host
        self.request_format = request_format

        self.max_ips = max_ips
        self.num_workers = num_workers
        self.timeout = timeout
        self.randomized = randomized

        self.running = False
        self.scanned = self.found = 0

    def cancel(self):
        self.running = False

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(self._run_async())
        finally:
            loop.close()

    async def _monitor(self):
        await asyncio.sleep(self.timeout)
        last_count = 0
        while self.running:
            await asyncio.sleep(0.2)
            current_count = self.scanned
            delta = current_count - last_count
            if delta > 0:
                self.progressUpdate.emit(delta)
                last_count = current_count

    async def _worker(self, queue, session):
        while True:
            ip = await queue.get()
            if not ip:
                break
            result = await test_ip(session, ip, self.host, self.request_format)
            if isinstance(result, float):
                self.foundAvailable.emit(ip, result)
                self.found += 1
            self.scanned += 1
            queue.task_done()

    async def _run_async(self):
        self.running = True
        self.scanned = self.found = 0
        queue = asyncio.Queue(maxsize=self.num_workers * 2)
        async with get_session(self.timeout) as session:
            workers = [
                asyncio.create_task(self._worker(queue, session))
                for _ in range(self.num_workers)
            ]
            monitor = asyncio.create_task(self._monitor())
            warmup_left = self.num_workers
            warmup_delay = 2 * self.timeout / self.num_workers
            for ip in ip_generator(self.networks, self.randomized):
                if not self.running or self.found >= self.max_ips:
                    break
                await queue.put(ip)
                if warmup_left > 0:
                    await asyncio.sleep(warmup_delay)
                    warmup_left -= 1
            for _ in range(self.num_workers):
                await queue.put(None)
            await asyncio.gather(*workers)
            self.running = False
            await monitor


class DebugThread(QThread):
    success = Signal(float)  # latency
    fail = Signal(str, str)  # reason: (type, message)

    def __init__(self, parent, ip, host, request_format, timeout, repeat):
        super().__init__(parent)

        self.ip = ip
        self.host = host
        self.request_format = request_format
        self.timeout = timeout
        self.repeat = repeat

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(self.run_async())
        finally:
            loop.close()

    async def run_async(self):
        async with get_session(self.timeout) as session:
            for _ in range(self.repeat):
                result = await test_ip(session, self.ip, self.host, self.request_format)
                if isinstance(result, float):
                    self.success.emit(result)
                else:
                    self.fail.emit(*result)
                await asyncio.sleep(0.05)
