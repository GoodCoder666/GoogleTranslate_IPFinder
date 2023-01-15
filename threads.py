# -*- coding: utf-8 -*-
from PySide6.QtCore import QThread, QThreadPool, QRunnable, QObject, Signal
from utils import test_ip, check_ip, dns_query
from ipaddress import IPv4Network


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
    available_suffixes = {90, 160, 161, 162, 163, 192}

    def __init__(self, parent, max_ips=5, num_workers=80, timeout=2.5, enableOptimization=True, query_ipv6=False):
        super().__init__(parent)

        self.max_ips = max_ips
        self.num_workers = num_workers
        self.timeout = timeout
        self.enableOptimization = enableOptimization
        self.query_ipv6 = query_ipv6
    
    def __found_available(self, ip):
        if self.counter >= self.max_ips:
            return
        self.counter += 1
        self.foundAvailable.emit(ip)
        if self.counter >= self.max_ips:
            self.pool.clear()

    def run(self):
        self.pool = QThreadPool()
        self.pool.setMaxThreadCount(self.num_workers)
        self.counter = 0
        if self.query_ipv6:
            for ip in dns_query(server='1.1.1.1', type='AAAA'):
                task = _ScanTask(ip, self.timeout)
                task.signals.foundAvailable.connect(self.__found_available)
                self.pool.start(task)
        for ip in IPv4Network('142.250.0.0/15'):
            if self.enableOptimization and int(ip) & 0xff not in self.available_suffixes:
                continue
            task = _ScanTask(str(ip), self.timeout)
            task.signals.foundAvailable.connect(self.__found_available)
            self.pool.start(task)
        self.pool.waitForDone()