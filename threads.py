from PySide6.QtCore import QThread, Signal
from utils import test_ip

class SpeedtestThread(QThread):
    foundAvailable = Signal(str, float) # foundAvailable(ip, seconds)
    foundUnavaliable = Signal(str, str) # foundUnavaliable(ip, reason)

    def __init__(self, parent, ips):
        super().__init__(parent)
        self.ips = ips

    def run(self):
        for ip in self.ips:
            result = test_ip(ip)
            if isinstance(result, str):
                self.foundUnavaliable.emit(ip, result)
            else:
                self.foundAvailable.emit(ip, result)
        self.exit(0)