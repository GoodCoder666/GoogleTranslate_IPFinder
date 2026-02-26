# -*- coding: utf-8 -*-
from html import escape

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Slot
from PySide6.QtGui import QTextCursor

from src.core.threads import DebugThread
from src.ui.generated.ui_dlgDebug import Ui_Dialog
from src.core.utils import time_repr


__all__ = ['dlgDebug']


class dlgDebug(QDialog):
    def __init__(self, parent, ip, host, request_format):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.ipEdit.setText(ip)
        self.ui.hostEdit.setText(host)
        self.ui.formatEdit.setText(request_format)

    @Slot()
    def on_btnDebug_clicked(self):
        self.ui.btnDebug.setEnabled(False)
        self.currentIP = self.ui.ipEdit.text()
        thread = DebugThread(self, self.currentIP, self.ui.hostEdit.text(), self.ui.formatEdit.text(),
                             self.ui.spinBox_timeout.value(), self.ui.spinBox_times.value())
        thread.success.connect(self._success)
        thread.fail.connect(self._fail)
        thread.finished.connect(lambda: self.ui.btnDebug.setEnabled(True))
        thread.start()

    def _insertHtml(self, html):
        self.ui.textBrowser.moveCursor(QTextCursor.End)
        self.ui.textBrowser.insertHtml(html)
        self.ui.textBrowser.moveCursor(QTextCursor.End)

    def _success(self, response_time):
        self._insertHtml(f'<font color="green"><b>成功 [{self.currentIP}]：响应时间 {time_repr(response_time)}</b></font><br/>')

    def _fail(self, error_type, message):
        self._insertHtml(f'<font color="red"><b>失败 [{self.currentIP}]：({error_type}) {escape(message)}</b></font><br/>')
