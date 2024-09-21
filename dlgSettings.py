# -*- coding: utf-8 -*-
from PySide6.QtWidgets import *
from PySide6.QtCore import Slot, Qt

from ui_dlgSettings import Ui_Dialog
from constants import DefaultConfig

__all__ = ['dlgSettings']

class dlgSettings(QDialog):
    idx_to_lang = ['zh_CN', 'en_US']
    lang_to_idx = {lang: idx for idx, lang in enumerate(idx_to_lang)}

    def __init__(self, parent, settings, default_font):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setText(self.tr('确定'))
        self.ui.buttonBox.button(QDialogButtonBox.Cancel).setText(self.tr('取消'))
        style_names = QStyleFactory.keys()
        self.ui.comboBox_style.addItems(style_names)
        self.default_font = default_font

        # initialize settings
        self.ui.comboBox_language.setCurrentIndex(self.lang_to_idx[settings.value('appearance/language')])
        style_name = settings.value('appearance/style')
        if style_name not in style_names:
            style_name = style_name.capitalize()
        self.ui.comboBox_style.setCurrentIndex(style_names.index(style_name))
        font = settings.value('appearance/font')
        self.ui.fontComboBox.setCurrentFont(font.family())
        self.ui.spinBox_fontSize.setValue(font.pointSize())
        self.ui.hostEdit.setText(settings.value('test/host'))
        self.ui.templateEdit.setText(settings.value('test/template'))
        self.ui.spinBox_threads.setValue(settings.value('test/num_threads', type=int))
        self.ui.doubleSpinBox_timeout.setValue(settings.value('test/timeout', type=float))
        self.ui.spinBox_repeat.setValue(settings.value('test/repeat', type=int))
        self._set_save_hosts(settings.value('saveHosts'))

    def _set_save_hosts(self, hosts):
        self.ui.saveHostsList.clear()
        for host in hosts:
            item = QListWidgetItem(host)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.ui.saveHostsList.addItem(item)

    def _get_save_hosts(self):
        return list(filter(lambda x: len(x.strip()) > 0, (
            self.ui.saveHostsList.item(i).text()
            for i in range(self.ui.saveHostsList.count())
        )))

    def apply(self, settings):
        settings.setValue('appearance/language', self.idx_to_lang[self.ui.comboBox_language.currentIndex()])
        settings.setValue('appearance/style', self.ui.comboBox_style.currentText())
        font = QApplication.font()
        font.setFamily(self.ui.fontComboBox.currentFont().family())
        font.setPointSize(self.ui.spinBox_fontSize.value())
        settings.setValue('appearance/font', font)
        settings.setValue('test/host', self.ui.hostEdit.text())
        settings.setValue('test/template', self.ui.templateEdit.text())
        settings.setValue('test/num_threads', self.ui.spinBox_threads.value())
        settings.setValue('test/timeout', self.ui.doubleSpinBox_timeout.value())
        settings.setValue('test/repeat', self.ui.spinBox_repeat.value())
        settings.setValue('saveHosts', self._get_save_hosts())
        settings.sync()

    @Slot()
    def on_btnRestoreDefaults_clicked(self):
        self.ui.comboBox_language.setCurrentIndex(self.lang_to_idx[DefaultConfig.language])
        self.ui.comboBox_style.setCurrentIndex(0)
        self.ui.fontComboBox.setCurrentFont(self.default_font)
        self.ui.spinBox_fontSize.setValue(self.default_font.pointSize())
        self.ui.hostEdit.setText(DefaultConfig.test_host)
        self.ui.templateEdit.setText(DefaultConfig.template)
        self.ui.spinBox_threads.setValue(DefaultConfig.num_threads)
        self.ui.doubleSpinBox_timeout.setValue(DefaultConfig.timeout)
        self.ui.spinBox_repeat.setValue(DefaultConfig.repeat)
        self._set_save_hosts(DefaultConfig.save_hosts)

    @Slot()
    def on_btnAddHost_clicked(self):
        self.ui.saveHostsList.clearSelection()
        item = QListWidgetItem()
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.ui.saveHostsList.addItem(item)
        self.ui.saveHostsList.setCurrentItem(item)
        self.ui.saveHostsList.editItem(item)

    @Slot()
    def on_btnRemoveHost_clicked(self):
        for item in self.ui.saveHostsList.selectedItems():
            self.ui.saveHostsList.takeItem(self.ui.saveHostsList.row(item))
