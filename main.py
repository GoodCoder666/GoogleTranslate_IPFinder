# -*- coding: utf-8 -*-
import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Slot

from dlgScan import dlgScan
from dlgImport import dlgImport
from threads import ScanThread, SpeedtestThread
from ui_MainWindow import Ui_MainWindow
from utils import DEFAULT_IPS, HOST, time_repr, read_url


app = QApplication(sys.argv)


class QTableWidgetTimeItem(QTableWidgetItem):
    def __init__(self, secs, time_str):
        super().__init__(time_str)
        self.secs = secs

    def __lt__(self, other):
        return self.secs < other.secs


class MainWindow(QMainWindow):
    SUPPORTED_FILTERS = '文本文件(*.txt);;所有文件(*.*)'

    def __init__(self, parent=None):
        # Initialize window
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.resultTable.setHorizontalHeaderLabels(['IP', '响应时间'])
        self.ui.resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.resultTable.sortItems(1, Qt.AscendingOrder)

        for ip in DEFAULT_IPS:
            self.ui.ipList.addItem(QListWidgetItem(ip))
        
        self.clipboard = QApplication.clipboard()

    def __replace_ips(self, ips):
        self.ui.ipList.clear()
        for ip in ips:
            if ip := ip.rstrip():
                self.ui.ipList.addItem(QListWidgetItem(ip))
        self.ui.statusbar.showMessage(f'导入成功，共 {len(ips)} 条 IP。')

    def __add_ips(self, ips):
        original_ips = {self.ui.ipList.item(i).text() for i in range(self.ui.ipList.count())}
        count = 0
        for ip in ips:
            ip = ip.rstrip()
            if ip and ip not in original_ips:
                self.ui.ipList.addItem(QListWidgetItem(ip))
                count += 1
        self.ui.statusbar.showMessage(f'导入成功，新增 {count} 条 IP。')

    def __save_ips(self, filename):
        with open(filename, 'w') as file:
            for row in range(self.ui.resultTable.rowCount()):
                file.write(self.ui.resultTable.item(row, 0).text() + '\n')

    @Slot()
    def on_btnWait_Import_clicked(self):
        dlg = dlgImport(self)
        if dlg.exec() != QDialog.Accepted:
            return
        new_ips = None
        if dlg.ui.radioLocalFile.isChecked():
            filename, _ = QFileDialog.getOpenFileName(self, '导入', filter=self.SUPPORTED_FILTERS)
            if not filename: return
            with open(filename, 'r') as file:
                new_ips = file.readlines()
        elif dlg.ui.radioSingleIP.isChecked():
            new_ips = [dlg.ui.singleIPEdit.text()]
        elif dlg.ui.radioCustomURL.isChecked():
            url = dlg.ui.customURLEdit.text()
            try:
                new_ips = read_url(url)
            except Exception:
                QMessageBox.critical(self, '错误', f'{url} 获取失败。请检查网络状况，然后再试。')
        else: # radioOnline
            SERVICES = (
                # (checkBox, timeout, (url, [alternative_urls]))
                (
                    dlg.ui.chkBox_std4,
                    3.5,
                    (
                        'https://unpkg.com/@hcfy/google-translate-ip/ips.txt',
                        'https://ghproxy.com/https://raw.githubusercontent.com/hcfyapp/google-translate-cn-ip/master/packages/google-translate-ip/ips.txt',
                        'https://cdn.jsdelivr.net/npm/@hcfy/google-translate-ip/ips.txt'
                    )
                ),
                (
                    dlg.ui.chkBox_ext4,
                    3.5,
                    (
                        'https://gitcode.net/mirrors/Ponderfly/GoogleTranslateIpCheck/-/raw/master/src/GoogleTranslateIpCheck/GoogleTranslateIpCheck/ip.txt',
                        'https://ghproxy.com/https://raw.githubusercontent.com/Ponderfly/GoogleTranslateIpCheck/master/src/GoogleTranslateIpCheck/GoogleTranslateIpCheck/ip.txt',
                        'https://raw.githubusercontent.com/Ponderfly/GoogleTranslateIpCheck/master/src/GoogleTranslateIpCheck/GoogleTranslateIpCheck/ip.txt'
                    )
                ),
                (
                    dlg.ui.chkBox_std6,
                    3.5,
                    (
                        'https://gitcode.net/mirrors/Ponderfly/GoogleTranslateIpCheck/-/raw/master/src/GoogleTranslateIpCheck/GoogleTranslateIpCheck/IPv6.txt',
                        'https://ghproxy.com/https://raw.githubusercontent.com/Ponderfly/GoogleTranslateIpCheck/master/src/GoogleTranslateIpCheck/GoogleTranslateIpCheck/IPv6.txt',
                        'https://raw.githubusercontent.com/Ponderfly/GoogleTranslateIpCheck/master/src/GoogleTranslateIpCheck/GoogleTranslateIpCheck/IPv6.txt'
                    )
                )
            )
            new_ips = set()
            for checkBox, timeout, urls in SERVICES:
                if checkBox.isChecked():
                    for url in urls:
                        try:
                            current_ips = read_url(url, timeout)
                        except Exception:
                            continue
                        break
                    else:
                        QMessageBox.critical(self, '错误', f'{checkBox.text()} 获取失败。请检查网络状况，然后再试。')
                        return
                    new_ips |= current_ips
        if dlg.ui.radioReplace.isChecked():
            self.__replace_ips(new_ips)
        else:
            self.__add_ips(new_ips)

    @Slot()
    def on_btnResult_Save_clicked(self):
        filename, _ = QFileDialog.getSaveFileName(self, '导出', filter=self.SUPPORTED_FILTERS)
        if not filename: return
        self.__save_ips(filename)
        self.ui.statusbar.showMessage(f'成功导出IP测速结果文件 [{filename}]')

    @Slot()
    def on_btnResult_Copy_clicked(self):
        if self.ui.resultTable.rowCount() == 0:
            QMessageBox.critical(self, '错误', '请先测速后再复制。')
            return
        self.ui.resultTable.sortItems(1, Qt.AscendingOrder)
        fastest_ip = self.ui.resultTable.item(0, 0).text()
        new_hosts = f'{fastest_ip} {HOST}'
        self.clipboard.setText(new_hosts)
        self.ui.statusbar.showMessage(f'成功复制最佳IP [{new_hosts}]')

    def __writeHosts(self, ip):
        hosts_path = r'C:\Windows\System32\drivers\etc\hosts' if sys.platform == 'win32' else '/etc/hosts'

        try:
            with open(hosts_path, 'r') as file:
                lines = file.readlines()
        except UnicodeDecodeError:
            with open(hosts_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

        encoding = file.encoding

        host_line = -1
        for idx, line in enumerate(lines):
            host_pos = line.find(HOST)
            comment_pos = line.find('#')
            if host_pos != -1 and (comment_pos == -1 or host_pos < comment_pos):
                host_line = idx

        changed_line = f'{ip} {HOST}'
        if host_line == -1:
            with open(hosts_path, 'a', encoding=encoding) as file:
                file.write('\n' + changed_line)
        else:
            lines[host_line] = changed_line + '\n'
            with open(hosts_path, 'w', encoding=encoding) as file:
                file.writelines(lines)

    @Slot()
    def on_btnResult_WriteHosts_clicked(self):
        if self.ui.resultTable.rowCount() == 0:
            QMessageBox.critical(self, '错误', '请先测速后再写入Hosts。')
            return
        self.ui.resultTable.sortItems(1, Qt.AscendingOrder)
        fastest_ip = self.ui.resultTable.item(0, 0).text()
        try:
            self.__writeHosts(fastest_ip)
        except PermissionError:
            QMessageBox.critical(self, '错误', '无权限访问Hosts文件。请检查程序权限，然后再试。\n您也可尝试复制IP后手动写入。')
            return
        except Exception as e:
            QMessageBox.critical(self, '错误', f'未知错误：{e}\n若此错误反复出现，请在issues中提出。')
            return
        self.ui.statusbar.showMessage(f'成功写入Hosts [{fastest_ip} {HOST}]')

    def __set_buttons_enabled(self, enabled):
        self.ui.btnResult_Copy.setEnabled(enabled)
        self.ui.btnResult_Save.setEnabled(enabled)
        self.ui.btnResult_WriteHosts.setEnabled(enabled)
        self.ui.btnWait_Import.setEnabled(enabled)
        self.ui.btnWait_Scan.setEnabled(enabled)
        self.ui.btnWait_Test.setEnabled(enabled)

    def __add_result(self, ip, seconds):
        self.ui.resultTable.setSortingEnabled(False) # TODO: maybe there's a better way to temporarily disable sorting?

        row = self.ui.resultTable.rowCount()
        self.ui.resultTable.setRowCount(row + 1)
        self.ui.resultTable.setItem(row, 0, QTableWidgetItem(ip))
        time_str = time_repr(seconds)
        self.ui.resultTable.setItem(row, 1, QTableWidgetTimeItem(seconds, time_str))
        self.ui.statusbar.showMessage(f'发现可用IP: {ip} [{time_str}]')

        self.ui.resultTable.setSortingEnabled(True)
    
    def __found_unavailable(self, ip, reason):
        self.ui.statusbar.showMessage(f'IP {ip} 不可用 [原因: {reason}]')

    def __speedtest_finished(self):
        self.__set_buttons_enabled(True)
        self.ui.statusbar.showMessage('测速完成')

    def __test_ips(self):
        self.ui.resultTable.setRowCount(0)
        ips = [self.ui.ipList.item(i).text() for i in range(self.ui.ipList.count())]
        thread = SpeedtestThread(self, ips, self.__add_result, self.__found_unavailable, num_workers=24)
        thread.finished.connect(self.__speedtest_finished)
        thread.start()

    @Slot()
    def on_btnWait_Test_clicked(self):
        self.__set_buttons_enabled(False)
        self.__test_ips()

    def __got_scan_result(self, ip):
        self.ui.ipList.addItem(QListWidgetItem(ip))
        self.ui.statusbar.showMessage(f'发现可用IP: {ip}')

    def __scan_finished(self):
        self.__set_buttons_enabled(True)
        self.ui.statusbar.showMessage('扫描完成')

    @Slot()
    def on_btnWait_Scan_clicked(self):
        dlg = dlgScan(self)
        if dlg.exec() == QDialog.Accepted:
            max_ips = dlg.ui.spinBox_MaxIP.value()
            num_workers = int(dlg.ui.comboBox_threads.currentText())
            timeout = dlg.ui.spinBox_timeout.value()
            enableOptimization = dlg.ui.chkBox_optimize.isChecked()
            autoTest = dlg.ui.chkBox_autoTest.isChecked()
            extend4 = dlg.ui.chkBox_extend4.isChecked()
            extend6 = dlg.ui.chkBox_extend6.isChecked()

            self.__set_buttons_enabled(False)
            self.ui.ipList.clear()
            self.ui.statusbar.showMessage('开始扫描，请稍候...')
            thread = ScanThread(self, max_ips, num_workers, timeout, enableOptimization, extend4, extend6)
            thread.finished.connect(self.__test_ips if autoTest else self.__scan_finished)
            thread.foundAvailable.connect(self.__got_scan_result)
            thread.start()

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        filename = event.mimeData().text()[8:] # [8:] is to get rid of 'file:///'
        with open(filename, 'r') as file:
            self.__replace_ips(file.readlines())


mainform = MainWindow()
mainform.show()

sys.exit(app.exec())
