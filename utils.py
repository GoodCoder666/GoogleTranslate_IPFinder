# -*- coding: utf-8 -*-
from json import JSONDecoder
from time import time
from urllib.request import Request, urlopen

__all__ = ['test_ip', 'check_ip', 'time_repr', 'dns_query', 'HOST', 'DEFAULT_IPS']

HOST = 'translate.googleapis.com'
HEADERS = {'Host': HOST}
TESTIP_FORMAT = 'https://{}/translate_a/single?client=gtx&sl=en&tl=fr&q=a'

def _build_request(ip):
    url = TESTIP_FORMAT.format(ip)
    request = Request(url, headers=HEADERS)
    request.host = HOST
    return request

def test_ip(ip, timeout=2.5):
    try:
        req = _build_request(ip)
        start_time = time()
        with urlopen(req, timeout=timeout) as response:
            end_time = time()
    except Exception as e:
        return str(e)
    return end_time - start_time

def check_ip(ip, timeout=2.5):
    try:
        urlopen(_build_request(ip), timeout=timeout).close()
    except Exception:
        return False
    return True

def time_repr(secs):
    return f'{secs*1000:.0f}ms' if secs < 0.9995 else f'{secs:.2f}s'

def dns_query(name=HOST, server='1.1.1.1', type='A', path='/dns-query'):
    # https://github.com/stamparm/python-doh/blob/master/client.py
    req = Request(
        f'https://{server}{path}?name={name}&type={type}',
        headers={'Accept': 'application/dns-json'},
    )
    content = urlopen(req).read().decode()
    reply = JSONDecoder().decode(content)
    return [] if 'Answer' not in reply else [_['data'] for _ in reply['Answer']]

DEFAULT_IPS = ['142.250.30.90', '142.250.97.90', '172.253.115.90', '172.217.214.90', '172.217.204.90', '172.217.222.90', '142.250.4.90', '142.250.128.90', '172.253.114.90', '142.250.136.90', '172.253.124.90', '142.250.185.174', '142.250.218.14', '172.217.16.46', '172.253.123.90', '172.253.112.90', '172.253.116.90', '142.250.28.90', '172.217.195.90', '216.58.220.142', '172.217.192.90', '172.217.203.90', '172.217.31.142', '172.253.122.90', '142.250.31.90', '142.250.185.238', '142.250.189.206', '142.250.126.90', '142.250.203.142', '172.253.126.90', '142.250.27.90', '172.217.215.90', '216.58.209.174', '142.250.9.90', '172.217.13.142', '142.251.5.90', '142.251.9.90', '142.250.98.90', '142.251.10.138', '142.251.116.101', '142.250.96.90', '172.253.62.90', '216.58.214.14', '142.251.40.174', '142.250.125.90', '142.250.8.90', '172.217.0.46', '142.250.110.90', '142.250.111.90', '142.250.112.90', '142.250.12.90', '142.250.101.90', '142.250.10.90', '142.250.100.90', '142.250.0.90', '142.250.105.90', '142.250.11.90', '142.250.107.90', '108.177.122.90', '2607:f8b0:4001:c07::5a', '2404:6800:4008:c13::5a', '2404:6800:4008:c15::5a', '2404:6800:4003:c00::5a', '2404:6800:4003:c01::5a', '2404:6800:4003:c02::5a', '2607:f8b0:4023:1402::5a', '2607:f8b0:4023:1401::5a', '2607:f8b0:4023:401::5a', '2607:f8b0:4023:1::5a', '2607:f8b0:4023::5a']