# -*- coding: utf-8 -*-
import sys
from ipaddress import ip_network

from PySide6.QtWidgets import *
from PySide6.QtCore import QSettings, Qt, QTranslator, Slot
from PySide6.QtGui import QAction

from constants import GTDB_IPS, ONLINE_SERVICES, DefaultConfig
from dlgAbout import dlgAbout
from dlgDebug import dlgDebug
from dlgImport import dlgImport
from dlgScan import dlgScan
from dlgSettings import dlgSettings
from threads import ScanThread, SpeedtestThread
from ui_MainWindow import Ui_MainWindow
from utils import open_url, read_url, time_repr


app = QApplication(sys.argv)


class QTableWidgetTimeItem(QTableWidgetItem):
    def __init__(self, secs, time_str):
        super().__init__(time_str)
        self.secs = secs

    def __lt__(self, other):
        return self.secs < other.secs


class MainWindow(QMainWindow):
    SUPPORTED_INPUT_FILTERS = QMainWindow.tr('文本文件(*.txt);;所有文件(*.*)')
    SUPPORTED_OUTPUT_FILTERS = QMainWindow.tr('文本文件(*.txt);;CSV 表格(*.csv);;所有文件(*.*)')

    # English translator
    translator = QTranslator()
    assert translator.load('en_US.qm', ':/translations/translations')

    def __init__(self, parent=None):
        # Initialize window
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.default_font = QApplication.font()

        # Initialize table
        self.ui.resultTable.setHorizontalHeaderLabels(['IP', self.tr('响应时间')])
        self.ui.resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.resultTable.sortItems(1, Qt.AscendingOrder)

        for ip in GTDB_IPS:
            self.ui.ipList.addItem(QListWidgetItem(ip))

        # Add right-click menu
        self.ui.ipList.setContextMenuPolicy(Qt.CustomContextMenu)
        menu = QMenu(self)
        actDelete = QAction(self.tr('删除'), self, triggered=self._delete_ip)
        font = actDelete.font()
        font.setBold(True)
        actDelete.setFont(font)
        menu.addAction(actDelete)
        menu.addAction(QAction(self.tr('复制'), self, triggered=self._copy_ip))
        menu.addAction(QAction(self.tr('清空'), self, triggered=self.ui.ipList.clear))
        menu.addAction(QAction(self.tr('调试'), self, triggered=self._debug_ip))
        self.ui.ipList.customContextMenuRequested.connect(lambda pos: menu.exec(self.ui.ipList.mapToGlobal(pos)))

        # clipboard
        self.clipboard = QApplication.clipboard()

        # settings
        self.ui.actResetSettings.triggered.connect(self._reset_settings)
        self.settings = QSettings('GoodCoder666', 'IPFinder')
        if set(self.settings.allKeys()) == {
                'appearance/style', 'appearance/font', 'appearance/language', 'scan/ranges', 'test/host',
                'test/template', 'test/num_threads', 'test/timeout', 'test/repeat', 'saveHosts'}:
            self._update_ui()
        else:
            self._reset_settings()
            self.ui.statusbar.showMessage(self.tr('设置初始化完成'))

    def _copy_ip(self):
        ip = self.ui.ipList.currentItem().text()
        self.clipboard.setText(ip)
        self.ui.statusbar.showMessage(self.tr('已复制 %s 到剪切板。') % ip)

    def _delete_ip(self):
        ip = self.ui.ipList.currentItem().text()
        self.ui.ipList.takeItem(self.ui.ipList.currentRow())
        self.ui.statusbar.showMessage(self.tr('已删除 %s。') % ip)

    def _debug_ip(self):
        dlgDebug(self, self.ui.ipList.currentItem().text(),
                 self.settings.value('test/host'), self.settings.value('test/template')).exec()

    def _replace_ips(self, ips):
        self.ui.ipList.clear()
        for ip in ips:
            if ip := ip.rstrip():
                self.ui.ipList.addItem(QListWidgetItem(ip))
        self.ui.statusbar.showMessage(self.tr('导入成功，共 %n 条 IP。', '', len(ips)))

    def _add_ips(self, ips):
        original_ips = {self.ui.ipList.item(i).text() for i in range(self.ui.ipList.count())}
        count = 0
        for ip in ips:
            ip = ip.rstrip()
            if ip and ip not in original_ips:
                self.ui.ipList.addItem(QListWidgetItem(ip))
                count += 1
        self.ui.statusbar.showMessage(self.tr('导入成功，新增 %n 条 IP。', '', count))

    def _save_ips(self, filename):
        if filename.endswith('.csv'):
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(f'IP,{self.tr("响应时间")}(ms)\n')
                for row in range(self.ui.resultTable.rowCount()):
                    ip = self.ui.resultTable.item(row, 0).text()
                    ms = self.ui.resultTable.item(row, 1).secs * 1000
                    file.write(f'{ip},{ms}\n')
        else:
            with open(filename, 'w') as file:
                for row in range(self.ui.resultTable.rowCount()):
                    file.write(self.ui.resultTable.item(row, 0).text() + '\n')

    def _save_hosts_repr(self):
        return '/'.join(self.settings.value('saveHosts'))

    def _reset_settings(self):
        self.settings.clear()
        self.settings.setValue('appearance/style', QApplication.style().objectName())
        self.settings.setValue('appearance/font', self.default_font)
        self.settings.setValue('appearance/language', DefaultConfig.language)
        self.settings.setValue('scan/ranges', DefaultConfig.scan_ranges)
        self.settings.setValue('test/host', DefaultConfig.test_host)
        self.settings.setValue('test/template', DefaultConfig.template)
        self.settings.setValue('test/num_threads', DefaultConfig.num_threads)
        self.settings.setValue('test/timeout', DefaultConfig.timeout)
        self.settings.setValue('test/repeat', DefaultConfig.repeat)
        self.settings.setValue('saveHosts', DefaultConfig.save_hosts)
        self.settings.sync()
        self._update_ui()
        self.ui.statusbar.showMessage(self.tr('设置已重置。'))

    def _update_ui(self):
        app.setFont(self.settings.value('appearance/font'))
        app.setStyle(QStyleFactory.create(self.settings.value('appearance/style')))
        if self.settings.value('appearance/language') == 'en_US':
            app.installTranslator(self.translator)
        else:
            app.removeTranslator(self.translator)
        self.ui.retranslateUi(self)
        self.ui.resultTable.setHorizontalHeaderLabels(['IP', self.tr('响应时间')])

    @Slot()
    def on_btnWait_Import_clicked(self):
        dlg = dlgImport(self)
        if dlg.exec() != QDialog.Accepted:
            return
        new_ips = None
        if dlg.ui.radioLocalFile.isChecked():
            filename, _ = QFileDialog.getOpenFileName(self, self.tr('导入'), filter=self.SUPPORTED_INPUT_FILTERS)
            if not filename: return
            try:
                with open(filename, 'r') as file:
                    new_ips = file.readlines()
            except UnicodeDecodeError:
                try:
                    with open(filename, 'r', encoding='utf-8-sig') as file:
                        new_ips = file.readlines()
                except UnicodeDecodeError:
                    QMessageBox.critical(self, self.tr('错误'), self.tr('文件编码错误。请检查文件内容，然后再试。'))
                    return
        elif dlg.ui.radioSingleIP.isChecked():
            new_ips = [dlg.ui.singleIPEdit.text()]
        elif dlg.ui.radioCustomURL.isChecked():
            url = dlg.ui.customURLEdit.text()
            try:
                new_ips = read_url(url, timeout=5)
            except Exception:
                QMessageBox.critical(self, self.tr('错误'), self.tr('%s 获取失败。请检查网络状况，然后再试。') % url)
                return
        else: # radioOnline
            new_ips = set()
            timeout = 3.5
            for checkBox, urls in zip((dlg.ui.chkBox_off4, dlg.ui.chkBox_ext4, dlg.ui.chkBox_ext6,
                                       dlg.ui.chkBox_full4, dlg.ui.chkBox_full6),
                                      ONLINE_SERVICES):
                if checkBox.isChecked():
                    for url in urls:
                        try:
                            current_ips = read_url(url, timeout)
                        except Exception:
                            continue
                        break
                    else:
                        QMessageBox.critical(self, self.tr('错误'), self.tr('%s 获取失败。请检查网络状况，然后再试。') % checkBox.text())
                        return
                    new_ips |= current_ips
        if dlg.ui.radioReplace.isChecked():
            self._replace_ips(sorted(new_ips))
        else:
            self._add_ips(new_ips)

    @Slot()
    def on_btnResult_Save_clicked(self):
        filename, _ = QFileDialog.getSaveFileName(self, self.tr('导出'), filter=self.SUPPORTED_OUTPUT_FILTERS)
        if not filename: return
        self._save_ips(filename)
        self.ui.statusbar.showMessage(self.tr('成功导出 IP 测速结果文件 [%s]') % filename)

    @Slot()
    def on_btnResult_Copy_clicked(self):
        if self.ui.resultTable.rowCount() == 0:
            QMessageBox.critical(self, self.tr('错误'), self.tr('请先测速后再复制。'))
            return
        self.ui.resultTable.sortItems(1, Qt.AscendingOrder)
        fastest_ip = self.ui.resultTable.item(0, 0).text()
        self.clipboard.setText('\n'.join(f'{fastest_ip} {host}' for host in self.settings.value('saveHosts')))
        message = self.tr('成功复制最佳 IP [%s %s]') % (fastest_ip, self._save_hosts_repr())
        self.ui.statusbar.showMessage(message)

    def _update_hosts(self, ip, host):
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
            host_pos = line.find(host)
            comment_pos = line.find('#')
            if host_pos != -1 and (comment_pos == -1 or host_pos < comment_pos):
                host_line = idx

        changed_line = f'{ip} {host}'
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
            QMessageBox.critical(self, self.tr('错误'), self.tr('请先测速后再写入Hosts。'))
            return
        if selectedIndexes := self.ui.resultTable.selectedIndexes():
            row = selectedIndexes[0].row()
        else:
            self.ui.resultTable.sortItems(1, Qt.AscendingOrder)
            row = 0
        selected_ip = self.ui.resultTable.item(row, 0).text()
        try:
            for host in self.settings.value('saveHosts'):
                self._update_hosts(selected_ip, host)
        except PermissionError:
            QMessageBox.critical(self, self.tr('错误'), self.tr('无权限访问Hosts文件。请检查程序权限，然后再试。\n您也可尝试复制IP后手动写入。'))
            return
        except Exception as e:
            QMessageBox.critical(self, self.tr('错误'), self.tr('未知错误：%s\n若此错误反复出现，请在issues中提出。') % e)
            return
        message = self.tr('成功写入 Hosts [%s %s]') % (selected_ip, self._save_hosts_repr())
        self.ui.statusbar.showMessage(message)

    def _set_buttons_enabled(self, enabled):
        self.ui.btnResult_Copy.setEnabled(enabled)
        self.ui.btnResult_Save.setEnabled(enabled)
        self.ui.btnResult_WriteHosts.setEnabled(enabled)
        self.ui.btnWait_Import.setEnabled(enabled)
        self.ui.btnWait_Scan.setEnabled(enabled)
        self.ui.btnWait_Test.setEnabled(enabled)

    def _init_progessBar(self, prog_max):
        self.progressBar = QProgressBar(self)
        self.progressBar.setFixedWidth(390)
        self.progressBar.setRange(0, prog_max)
        self.progressBar.setValue(0)
        self.logLabel = QLabel(self)
        self.logLabel.setMaximumWidth(370)
        self.ui.statusbar.clearMessage()
        self.ui.statusbar.addWidget(self.progressBar)
        self.ui.statusbar.addWidget(self.logLabel)

    def _update_progressBar(self, dt=1):
        self.progressBar.setValue(self.progressBar.value() + dt)

    def _scan_update(self, dt):
        self._update_progressBar(dt)
        self.logLabel.setText(self.tr('已扫描: %s / %s') % (self.progressBar.value(), self.progressBar.maximum()))

    def _remove_progessBar(self):
        self.progressBar.deleteLater()
        self.logLabel.deleteLater()

    def _add_result(self, ip, seconds):
        self.ui.resultTable.setSortingEnabled(False) # TODO: maybe there's a better way to temporarily disable sorting?

        row = self.ui.resultTable.rowCount()
        self.ui.resultTable.setRowCount(row + 1)
        self.ui.resultTable.setItem(row, 0, QTableWidgetItem(ip))
        time_str = time_repr(seconds)
        self.ui.resultTable.setItem(row, 1, QTableWidgetTimeItem(seconds, time_str))
        self.logLabel.setText(self.tr('发现可用IP: %s [%s]') % (ip, time_str))
        self._update_progressBar()

        self.ui.resultTable.setSortingEnabled(True)

    def _found_unavailable(self, ip, reason):
        self.logLabel.setText(self.tr('IP %s 不可用 [原因: %s]') % (ip, reason))
        self._update_progressBar()

    def _speedtest_finished(self):
        self._set_buttons_enabled(True)
        self._remove_progessBar()
        self.ui.statusbar.showMessage(self.tr('测速完成'))

    def _test_ips(self, after_scan=True):
        self.ui.resultTable.setRowCount(0)
        ips = [self.ui.ipList.item(i).text() for i in range(self.ui.ipList.count())]
        if after_scan:
            self.progressBar.setValue(0)
            self.progressBar.setMaximum(len(ips))
            self.ui.btnWait_Scan.setText(self.tr('扫描'))
            self.ui.btnWait_Scan.setEnabled(False)
        else:
            self._init_progessBar(len(ips))
        thread = SpeedtestThread(self, ips,
                                 host=self.settings.value('test/host'),
                                 request_format=self.settings.value('test/template'),
                                 available_callback=self._add_result,
                                 unavailable_callback=self._found_unavailable,
                                 timeout=self.settings.value('test/timeout', type=float),
                                 repeat=self.settings.value('test/repeat', type=int),
                                 num_workers=self.settings.value('test/num_threads', type=int))
        thread.finished.connect(self._speedtest_finished)
        thread.start()

    @Slot()
    def on_btnWait_Test_clicked(self):
        self._set_buttons_enabled(False)
        self._test_ips(False)

    def _report_single_scan_result(self, ip):
        self.ui.ipList.addItem(QListWidgetItem(ip))
        self.logLabel.setText(self.tr('发现可用IP: %s') % ip)

    def _after_scan(self):
        self._set_buttons_enabled(True)
        self.ui.btnWait_Scan.setText(self.tr('扫描'))
        self._remove_progessBar()
        self.ui.statusbar.showMessage(self.tr('扫描完成'))

    @Slot()
    def on_btnWait_Scan_clicked(self):
        if self.ui.btnWait_Scan.text() == self.tr('取消'):
            self.ui.btnWait_Scan.setEnabled(False)
            self.sthread.cancel()
            return

        dlg = dlgScan(self, self.settings.value('scan/ranges'))
        if dlg.exec() == QDialog.Accepted:
            max_ips = dlg.ui.spinBox_MaxIP.value()
            num_workers = int(dlg.ui.comboBox_threads.currentText())
            timeout = dlg.ui.spinBox_timeout.value()
            autoTest = dlg.ui.chkBox_autoTest.isChecked()
            randomized = dlg.ui.chkBox_randomizeScan.isChecked()

            # process IP ranges
            ip_ranges = dlg.ip_ranges
            try:
                ip_networks = [ip_network(ip_range) for enabled, ip_range, _ in ip_ranges if enabled]
            except ValueError:
                for enabled, ip_range, _ in ip_ranges:
                    if not enabled: continue
                    try:
                        ip_network(ip_range)
                    except ValueError:
                        QMessageBox.critical(self, self.tr('错误'), self.tr('%s 不是一个合法的 IP 段。') % ip_range)
                        return
            if not ip_networks:
                QMessageBox.critical(self, self.tr('错误'), self.tr('请至少选择一个 IP 段。'))
                return
            self.settings.setValue('scan/ranges', ip_ranges)

            self._set_buttons_enabled(False)
            self.ui.ipList.clear()

            thread = ScanThread(self, ip_networks, max_ips, num_workers, timeout, randomized)
            thread.finished.connect(self._test_ips if autoTest else self._after_scan)
            thread.foundAvailable.connect(self._report_single_scan_result)
            thread.progressUpdate.connect(self._scan_update)
            total_addrs = sum(map(len, thread.networks))
            self._init_progessBar(total_addrs)
            self.logLabel.setText(self.tr('开始扫描，共 %n 个 IP...', '', total_addrs))
            thread.start()

            self.sthread = thread
            self.ui.btnWait_Scan.setEnabled(True)
            self.ui.btnWait_Scan.setText(self.tr('取消'))

    @Slot()
    def on_actSettings_triggered(self):
        dlg = dlgSettings(self, self.settings, self.default_font)
        if dlg.exec() == QDialog.Accepted:
            dlg.apply(self.settings)
            self._update_ui()
            self.ui.statusbar.showMessage(self.tr('设置已更新。'))

    @Slot()
    def on_actProjectHomepage_triggered(self):
        open_url('https://github.com/GoodCoder666/GoogleTranslate_IPFinder')

    @Slot()
    def on_actCheckUpdates_triggered(self):
        open_url('https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases')

    @Slot()
    def on_actAbout_triggered(self):
        dlgAbout(self).exec()

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        filename = event.mimeData().text()[8:] # [8:] is to get rid of 'file:///'
        with open(filename, 'r') as file:
            self._replace_ips(file.readlines())


mainform = MainWindow()
mainform.show()

sys.exit(app.exec())
