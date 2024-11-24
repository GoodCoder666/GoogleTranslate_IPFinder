# -*- coding: utf-8 -*-
from PySide6.QtCore import QThread, QThreadPool, QRunnable, QObject, Signal
from utils import test_ip, check_ip
from constants import DefaultConfig
import random


__all__ = ['SpeedtestThread', 'ScanThread']


class _SpeedtestTaskSignals(QObject):
    foundAvailable = Signal(str, float) # foundAvailable(ip, seconds)
    foundUnavailable = Signal(str, str) # foundUnavailable(ip, reason)


class _SpeedtestTask(QRunnable):
    def __init__(self, ip, host, request_format, timeout=2.5, repeat=3):
        super().__init__()

        self.ip = ip
        self.host = host
        self.request_format = request_format
        self.timeout = timeout
        self.repeat = repeat
        self.signals = _SpeedtestTaskSignals()

    def run(self):
        total = 0
        for _ in range(self.repeat):
            result = test_ip(self.ip, self.timeout, self.host, self.request_format)
            if isinstance(result, str):
                self.signals.foundUnavailable.emit(self.ip, result)
                return
            total += result
        average = total / self.repeat
        self.signals.foundAvailable.emit(self.ip, average)


class SpeedtestThread(QThread):
    def __init__(self, parent, ips, host, request_format,
                 available_callback, unavailable_callback,
                 timeout=2.5, repeat=3, num_workers=8):
        super().__init__(parent)
        self.ips = ips
        self.host = host
        self.request_format = request_format
        self.available_callback = available_callback
        self.unavailable_callback = unavailable_callback
        self.timeout = timeout
        self.repeat = repeat
        self.num_workers = num_workers

    def run(self):
        pool = QThreadPool()
        pool.setMaxThreadCount(self.num_workers)
        for ip in self.ips:
            task = _SpeedtestTask(ip, self.host, self.request_format, self.timeout, self.repeat)
            task.signals.foundAvailable.connect(self.available_callback)
            task.signals.foundUnavailable.connect(self.unavailable_callback)
            pool.start(task)
            self.msleep(30)
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
        if check_ip(self.ip, self.timeout, DefaultConfig.test_host, DefaultConfig.template):
            self.signals.foundAvailable.emit(self.ip)


class ScanThread(QThread):
    foundAvailable = Signal(str)
    progressUpdate = Signal(int)

    def __init__(self, parent, ip_networks, max_ips=5, num_workers=80, timeout=2.5, randomized=False):
        super().__init__(parent)

        self.max_ips = max_ips
        self.num_workers = num_workers
        self.timeout = timeout

        self.networks = [list(net) for net in ip_networks]

        self.current_index = 0
        self.block_size = max(64, num_workers * 2)

        if randomized:
            for network in self.networks:
                random.shuffle(network)

    def _found_available(self, ip):
        if self.counter >= self.max_ips:
            return
        self.counter += 1
        self.foundAvailable.emit(ip)
        if self.counter >= self.max_ips:
            self.pool.clear()

    def _add_block(self):
        self.num_added = 0
        for _ in range(self.block_size):
            ok = False
            for net in self.networks:
                if self.current_index >= len(net):
                    continue
                ip = str(net[self.current_index])
                ok = True
                task = _ScanTask(ip, self.timeout)
                task.signals.foundAvailable.connect(self._found_available)
                self.pool.start(task)
                self.num_added += 1
            if not ok:
                return False
            self.current_index += 1
        return True

    def cancel(self):
        self.running = False

    def run(self):
        self.running = True
        self.pool = QThreadPool()
        self.pool.setMaxThreadCount(self.num_workers)
        self.counter = 0
        while self.running and self.counter < self.max_ips and self._add_block():
            self.pool.waitForDone()
            self.progressUpdate.emit(self.num_added)
        self.pool.waitForDone()


class DebugThread(QThread):
    success = Signal(float) # success(seconds)
    fail = Signal(str) # fail(reason)

    def __init__(self, parent, ip, host, request_format, timeout, repeat):
        super().__init__(parent)

        self.ip = ip
        self.host = host
        self.request_format = request_format
        self.timeout = timeout
        self.repeat = repeat

    def run(self):
        for _ in range(self.repeat):
            result = test_ip(self.ip, self.timeout, self.host, self.request_format)
            signal = self.fail if isinstance(result, str) else self.success
            signal.emit(result)
