# -*- coding: utf-8 -*-
from json import JSONDecoder
from time import time
from urllib.request import Request, urlopen
import ssl

__all__ = ['test_ip', 'check_ip', 'time_repr', 'dns_query', 'HOST', 'DEFAULT_IPS']

HOST = 'translate.googleapis.com'
TESTIP_FORMAT = 'https://{}/translate_a/single?client=gtx&sl=en&tl=fr&q=a'

def _build_request(ip):
    url = TESTIP_FORMAT.format(f'[{ip}]' if ':' in ip else ip)
    request = Request(url)
    request.add_header('Host', HOST)
    return request

def new_context():
    ctx = ssl.create_default_context()
    old_wrap_socket = ctx.wrap_socket

    def new_wrap_socket(socket, **kwargs):
        kwargs["server_hostname"] = HOST
        return old_wrap_socket(socket, **kwargs)

    ctx.wrap_socket = new_wrap_socket
    return ctx

def test_ip(ip, timeout=2.5):
    try:
        req = _build_request(ip)
        start_time = time()
        with urlopen(req, timeout=timeout, context=new_context()) as response:
            end_time = time()
    except Exception as e:
        if 'SSLV3' in str(e):
            print(ip)
        return str(e)
    return end_time - start_time

def check_ip(ip, timeout=2.5):
    try:
        urlopen(_build_request(ip), timeout=timeout, context=new_context()).close()
    except:
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

DEFAULT_IPS = ['172.217.204.90', '172.253.58.90', '142.250.189.206', '142.250.28.90', '142.251.107.90', '142.250.11.90', '142.250.185.238', '142.250.159.90', '142.250.31.90', '142.250.1.90', '172.217.0.46', '142.250.103.90', '142.251.40.174', '142.251.160.90', '142.250.9.90', '108.177.122.90', '142.250.128.90', '142.251.116.90', '172.253.112.90', '142.251.10.138', '142.250.126.90', '172.253.115.90', '108.177.111.90', '142.251.117.90', '142.250.107.90', '216.58.214.14', '142.250.111.90', '142.251.15.90', '142.250.185.174', '142.251.16.185', '142.250.101.90', '172.253.124.90', '172.217.203.90', '142.250.138.90', '142.250.98.90', '142.250.157.183', '142.251.18.90', '172.253.113.90', '142.250.113.90', '142.251.10.90', '142.250.157.184', '142.250.125.185', '172.217.215.90', '142.250.158.90', '142.250.114.90', '142.250.153.90', '108.177.125.186', '216.58.227.66', '172.217.195.90', '142.251.1.90', '172.253.122.90', '216.58.227.65', '142.250.145.90', '172.253.119.90', '142.251.8.90', '142.250.125.90', '108.177.127.90', '142.250.157.90', '142.251.2.90', '142.251.9.90', '142.250.8.90', '142.250.152.90', '142.250.105.90', '142.250.102.90', '142.250.217.185', '142.251.175.90', '142.251.171.90', '142.251.120.90', '172.217.222.90', '172.253.114.90', '216.58.227.67', '142.250.96.90', '142.250.4.185', '142.250.136.90', '172.253.126.90', '142.250.13.90', '142.251.166.90', '172.253.127.90', '142.250.30.90', '142.250.100.90', '142.250.157.186', '142.251.116.101', '108.177.97.100', '172.253.63.90', '142.250.218.14', '142.250.110.90', '142.250.0.90', '142.251.12.90', '142.250.112.90', '142.250.12.90', '172.217.16.46', '142.251.162.90', '172.217.214.90', '172.253.117.90', '142.250.141.90', '172.217.31.142', '142.250.123.90', '142.251.111.90', '142.251.172.90', '216.58.220.142', '142.250.10.90', '172.253.116.90', '142.251.0.90', '142.251.4.90', '142.250.4.90', '172.217.13.142', '142.250.203.142', '142.251.5.90', '142.251.163.90', '172.253.125.90', '142.251.112.90', '172.253.123.90', '142.250.142.90', '142.250.27.90', '142.251.12.185', '108.177.126.90', '142.250.99.90', '142.250.97.90', '142.251.16.90', '142.250.115.90', '142.251.6.90', '216.58.209.174', '172.217.192.90', '172.253.62.90', '172.253.118.90', '142.251.161.90']