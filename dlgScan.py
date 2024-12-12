# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtCore import Slot
from ui_dlgScan import Ui_Dialog
from dlgEditRange import dlgEditRange

__all__ = ['dlgScan']

class dlgScan(QDialog):
    def __init__(self, parent, ip_ranges):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.buttonBox.button(QDialogButtonBox.Ok).setText(self.tr('扫描'))
        self.ui.buttonBox.button(QDialogButtonBox.Cancel).setText(self.tr('取消'))

        self.ip_ranges = ip_ranges
        self._update_range_count()

    def _update_range_count(self):
        edit_translation = self.tr('编辑...')
        num_ranges = len(self.ip_ranges)
        num_enabled_ranges = sum(enabled for enabled, _, _ in self.ip_ranges)
        self.ui.btnEditRanges.setText(f'{edit_translation} ({num_enabled_ranges}/{num_ranges})')

    @Slot()
    def on_btnEditRanges_clicked(self):
        dlg = dlgEditRange(self, self.ip_ranges)
        if dlg.exec() == QDialog.Accepted:
            self.ip_ranges = dlg.get_ranges()
            self._update_range_count()