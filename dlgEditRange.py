# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt, Slot
from ui_dlgEditRange import Ui_Dialog
from constants import DefaultConfig

__all__ = ['dlgEditRange']

class dlgEditRange(QDialog):
    def __init__(self, parent, initial_ranges):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.buttonBox.button(QDialogButtonBox.Ok).setText(self.tr('更新'))
        self.ui.buttonBox.button(QDialogButtonBox.Cancel).setText(self.tr('取消'))

        self.ui.rangesTable.setHorizontalHeaderLabels([self.tr('IP 段'), self.tr('备注')])
        self.ui.rangesTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.rangesTable.setRowCount(len(initial_ranges))
        for i, (enabled, ip_range, notes) in enumerate(initial_ranges):
            range_item = QTableWidgetItem(ip_range)
            range_item.setCheckState(Qt.Checked if enabled else Qt.Unchecked)
            self.ui.rangesTable.setItem(i, 0, range_item)
            self.ui.rangesTable.setItem(i, 1, QTableWidgetItem(notes))

    def get_ranges(self):
        return [
            (self.ui.rangesTable.item(i, 0).checkState() == Qt.Checked,
             self.ui.rangesTable.item(i, 0).text(),
             self.ui.rangesTable.item(i, 1).text())
            for i in range(self.ui.rangesTable.rowCount())
        ]

    @Slot()
    def on_btnAdd_clicked(self):
        row = self.ui.rangesTable.rowCount()
        self.ui.rangesTable.setRowCount(row + 1)
        range_item = QTableWidgetItem('')
        range_item.setCheckState(Qt.Checked)
        self.ui.rangesTable.setItem(row, 0, range_item)
        self.ui.rangesTable.setItem(row, 1, QTableWidgetItem(''))
        self.ui.rangesTable.editItem(self.ui.rangesTable.item(row, 0))

    @Slot()
    def on_btnRemove_clicked(self):
        row = self.ui.rangesTable.currentRow()
        if row >= 0:
            self.ui.rangesTable.removeRow(row)

    @Slot()
    def on_btnReset_clicked(self):
        self.ui.rangesTable.setRowCount(len(DefaultConfig.scan_ranges))
        for i, (enabled, ip_range, notes) in enumerate(DefaultConfig.scan_ranges):
            range_item = QTableWidgetItem(ip_range)
            range_item.setCheckState(Qt.Checked if enabled else Qt.Unchecked)
            self.ui.rangesTable.setItem(i, 0, range_item)
            self.ui.rangesTable.setItem(i, 1, QTableWidgetItem(notes))

    @Slot()
    def on_btnClear_clicked(self):
        self.ui.rangesTable.setRowCount(0)
