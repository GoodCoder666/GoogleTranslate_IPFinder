# -*- coding: utf-8 -*-
from PySide6.QtCore import QThread, QThreadPool, QRunnable, QObject, Signal
from utils import test_ip, check_ip
from ipaddress import IPv4Network, IPv6Network


__all__ = ['SpeedtestThread', 'ScanThread']


class _SpeedtestTaskSignals(QObject):
    foundAvailable = Signal(str, float) # foundAvailable(ip, seconds)
    foundUnavailable = Signal(str, str) # foundUnavailable(ip, reason)


class _SpeedtestTask(QRunnable):
    def __init__(self, ip):
        super().__init__()

        self.ip = ip
        self.signals = _SpeedtestTaskSignals()

    def run(self):
        result = test_ip(self.ip)
        if isinstance(result, str):
            self.signals.foundUnavailable.emit(self.ip, result)
        else:
            self.signals.foundAvailable.emit(self.ip, result)


class SpeedtestThread(QThread):
    def __init__(self, parent, ips, available_callback, unavailable_callback, num_workers=8):
        super().__init__(parent)
        self.ips = ips
        self.available_callback = available_callback
        self.unavailable_callback = unavailable_callback
        self.num_workers = num_workers

    def run(self):
        pool = QThreadPool()
        pool.setMaxThreadCount(self.num_workers)
        for ip in self.ips:
            task = _SpeedtestTask(ip)
            task.signals.foundAvailable.connect(self.available_callback)
            task.signals.foundUnavailable.connect(self.unavailable_callback)
            pool.start(task)
            self.msleep(100)
        pool.waitForDone()


class _ScanTaskSignals(QObject):
    foundAvailable = Signal(str)


class _ScanTask(QRunnable):
    def __init__(self, ip, timeout):
        super().__init__()

        self.ip = ip
        self.timeout = timeout
        self.signals = _ScanTaskSignals()

    def run(self):
        if check_ip(self.ip, self.timeout):
            self.signals.foundAvailable.emit(self.ip)


class ScanThread(QThread):
    foundAvailable = Signal(str)
    available_suffixes = {90, 121, 218}

    # https://repo.or.cz/gscan_quic.git/blob/89e4b91eb3642b12f7665f7a9f4fa33c403fc318:/iprange_gws_b.txt
    net_default = IPv4Network('142.250.0.0/15')
    ipv4_extend = [
        IPv4Network('108.170.192.0/18'),
        IPv4Network('108.177.0.0/17'),
        IPv4Network('172.110.32.0/21'),
        IPv4Network('172.217.0.0/16'),
        IPv4Network('172.253.0.0/16'),
        IPv4Network('216.58.192.0/19'),
        IPv4Network('216.73.80.0/20'),
        IPv4Network('216.239.32.0/19')
    ]

    # https://repo.or.cz/gscan_quic.git/blob/89e4b91eb3642b12f7665f7a9f4fa33c403fc318:/iprange_gws_6_a.txt
    ipv6_extend = [
        IPv6Network('2a00:1450:4001:802::0/112'),
        IPv6Network('2a00:1450:4001:803::0/112'),
        IPv6Network('2a00:1450:4001:809::0/112'),
        IPv6Network('2a00:1450:4001:811::0/112'),
        IPv6Network('2a00:1450:4001:827::0/112'),
        IPv6Network('2a00:1450:4001:828::0/112'),
        IPv6Network('2a00:1450:4001:829::0/112'),
        IPv6Network('2a00:1450:4001:830::0/112'),
        IPv6Network('2a00:1450:4001:831::0/112')
    ]

    def __init__(self, parent, max_ips=5, num_workers=80, timeout=2.5,
                 enableOptimization=True, extendScan=False):
        super().__init__(parent)

        self.max_ips = max_ips
        self.num_workers = num_workers
        self.timeout = timeout

        self.networks = [
            [ip for ip in self.net_default if int(ip) & 0xff in self.available_suffixes]
            if enableOptimization else list(self.net_default)
        ]
        if extendScan:
            self.networks.extend(self.ipv4_extend)
            self.networks.extend(self.ipv6_extend)

        self.currentIndex = 0
        self.block_size = 15 if extendScan else max(15, self.num_workers // 4)
    
    def __found_available(self, ip):
        if self.counter >= self.max_ips:
            return
        self.counter += 1
        self.foundAvailable.emit(ip)
        if self.counter >= self.max_ips:
            self.pool.clear()

    def __add_block(self):
        for _ in range(self.block_size):
            ok = False
            for net in self.networks:
                try:
                    ip = str(net[self.currentIndex])
                except IndexError:
                    continue
                ok = True
                task = _ScanTask(ip, self.timeout)
                task.signals.foundAvailable.connect(self.__found_available)
                self.pool.start(task)
            if not ok:
                return False
            self.currentIndex += 1
        return True

    def run(self):
        self.pool = QThreadPool()
        self.pool.setMaxThreadCount(self.num_workers)
        self.counter = 0
        while self.counter < self.max_ips and self.__add_block():
            self.pool.waitForDone()