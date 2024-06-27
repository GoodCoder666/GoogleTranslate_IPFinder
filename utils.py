# -*- coding: utf-8 -*-
import ssl
import sys
from gzip import GzipFile
from time import time
from urllib.request import Request, urlopen

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

__all__ = ['test_ip', 'check_ip', 'time_repr', 'read_url', 'open_url']

def _build_request(ip, host, request_format):
    url = request_format.format(f'[{ip}]' if ':' in ip else ip)
    request = Request(url)
    request.add_header('Host', host)
    return request

def _new_context(host):
    ctx = ssl._create_unverified_context() if sys.platform.startswith('darwin') else ssl.create_default_context()
    old_wrap_socket = ctx.wrap_socket

    def new_wrap_socket(socket, **kwargs):
        kwargs['server_hostname'] = host
        return old_wrap_socket(socket, **kwargs)

    ctx.wrap_socket = new_wrap_socket
    return ctx

def test_ip(ip, timeout, host, request_format):
    try:
        req = _build_request(ip, host, request_format)
        start_time = time()
        with urlopen(req, timeout=timeout, context=_new_context(host)):
            end_time = time()
    except Exception as e:
        return str(e)
    return end_time - start_time

def check_ip(ip, timeout, host, request_format):
    try:
        req = _build_request(ip, host, request_format)
        urlopen(req, timeout=timeout, context=_new_context(host)).close()
    except:
        return False
    return True

def time_repr(secs):
    return f'{secs*1000:.0f}ms' if secs < 0.9995 else f'{secs:.2f}s'

def read_url(url, timeout):
    request = Request(url)
    request.add_header('Accept-Encoding', 'gzip')
    with urlopen(request, timeout=timeout) as response:
        # Handle gzip
        if response.getheader('Content-Encoding') == 'gzip':
            with GzipFile(fileobj=response) as gz:
                return {s.decode('utf-8').strip() for s in gz}
        return {s.decode('utf-8').strip() for s in response}

def open_url(url):
    QDesktopServices.openUrl(QUrl(url))
