# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from ui_dlgScan import Ui_Dialog

__all__ = ['dlgScan']

class dlgScan(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.buttonBox.button(QDialogButtonBox.Ok).setText(self.tr('扫描'))
        self.ui.buttonBox.button(QDialogButtonBox.Cancel).setText(self.tr('取消'))
