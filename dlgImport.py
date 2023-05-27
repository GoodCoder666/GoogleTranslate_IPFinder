# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtCore import Slot
from ui_dlgImport import Ui_Dialog

__all__ = ['dlgImport']

class dlgImport(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.buttonBox.button(QDialogButtonBox.Ok).setText('导入')
        self.ui.buttonBox.button(QDialogButtonBox.Cancel).setText('取消')