# -*- coding: utf-8 -*-
from html import escape

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Slot
from PySide6.QtGui import QTextCursor

from threads import DebugThread
from ui_dlgDebug import Ui_Dialog
from utils import HOST, TESTIP_FORMAT, time_repr

__all__ = ['dlgDebug']

class dlgDebug(QDialog):
    def __init__(self, parent, ip):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.ipEdit.setText(ip)
        self.ui.hostEdit.setText(HOST)
        self.ui.formatEdit.setText(TESTIP_FORMAT)

    @Slot()
    def on_btnDebug_clicked(self):
        self.ui.btnDebug.setEnabled(False)
        self.currentIP = self.ui.ipEdit.text()
        thread = DebugThread(self, self.currentIP, self.ui.hostEdit.text(), self.ui.formatEdit.text(),
                             self.ui.spinBox_timeout.value(), self.ui.spinBox_times.value())
        thread.success.connect(self.__success)
        thread.fail.connect(self.__fail)
        thread.finished.connect(lambda: self.ui.btnDebug.setEnabled(True))
        thread.start()

    def __insertHtml(self, html):
        self.ui.textBrowser.moveCursor(QTextCursor.End)
        self.ui.textBrowser.insertHtml(html)
        self.ui.textBrowser.moveCursor(QTextCursor.End)

    def __success(self, response_time):
        self.__insertHtml(f'<font color="green"><b>成功 [{self.currentIP}]：响应时间 {time_repr(response_time)}</b></font><br/>')

    def __fail(self, reason):
        self.__insertHtml(f'<font color="red"><b>失败 [{self.currentIP}]：{escape(reason)}</b></font><br/>')
