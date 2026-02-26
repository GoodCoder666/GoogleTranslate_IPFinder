# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlgSettings.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QComboBox,
    QDialog, QDialogButtonBox, QDoubleSpinBox, QFontComboBox,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(480, 574)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_appearance = QGroupBox(Dialog)
        self.groupBox_appearance.setObjectName(u"groupBox_appearance")
        self.gridLayout = QGridLayout(self.groupBox_appearance)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labStyle = QLabel(self.groupBox_appearance)
        self.labStyle.setObjectName(u"labStyle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labStyle.sizePolicy().hasHeightForWidth())
        self.labStyle.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.labStyle, 1, 0, 1, 2)

        self.fontComboBox = QFontComboBox(self.groupBox_appearance)
        self.fontComboBox.setObjectName(u"fontComboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fontComboBox.sizePolicy().hasHeightForWidth())
        self.fontComboBox.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.fontComboBox, 3, 1, 1, 2)

        self.comboBox_style = QComboBox(self.groupBox_appearance)
        self.comboBox_style.setObjectName(u"comboBox_style")
        sizePolicy1.setHeightForWidth(self.comboBox_style.sizePolicy().hasHeightForWidth())
        self.comboBox_style.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.comboBox_style, 1, 2, 1, 1)

        self.spinBox_fontSize = QSpinBox(self.groupBox_appearance)
        self.spinBox_fontSize.setObjectName(u"spinBox_fontSize")
        self.spinBox_fontSize.setMinimum(4)
        self.spinBox_fontSize.setMaximum(20)
        self.spinBox_fontSize.setValue(9)

        self.gridLayout.addWidget(self.spinBox_fontSize, 3, 3, 1, 1)

        self.labGlobalFont = QLabel(self.groupBox_appearance)
        self.labGlobalFont.setObjectName(u"labGlobalFont")
        sizePolicy.setHeightForWidth(self.labGlobalFont.sizePolicy().hasHeightForWidth())
        self.labGlobalFont.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.labGlobalFont, 3, 0, 1, 1)

        self.labLanguage = QLabel(self.groupBox_appearance)
        self.labLanguage.setObjectName(u"labLanguage")

        self.gridLayout.addWidget(self.labLanguage, 0, 0, 1, 1)

        self.comboBox_language = QComboBox(self.groupBox_appearance)
        self.comboBox_language.addItem("")
        self.comboBox_language.addItem("")
        self.comboBox_language.setObjectName(u"comboBox_language")

        self.gridLayout.addWidget(self.comboBox_language, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_appearance)

        self.groupBox_speedTest = QGroupBox(Dialog)
        self.groupBox_speedTest.setObjectName(u"groupBox_speedTest")
        self.gridLayout_2 = QGridLayout(self.groupBox_speedTest)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labRepeat = QLabel(self.groupBox_speedTest)
        self.labRepeat.setObjectName(u"labRepeat")
        sizePolicy.setHeightForWidth(self.labRepeat.sizePolicy().hasHeightForWidth())
        self.labRepeat.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.labRepeat, 7, 0, 1, 1)

        self.doubleSpinBox_timeout = QDoubleSpinBox(self.groupBox_speedTest)
        self.doubleSpinBox_timeout.setObjectName(u"doubleSpinBox_timeout")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_timeout.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_timeout.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_timeout.setDecimals(1)
        self.doubleSpinBox_timeout.setMinimum(0.500000000000000)
        self.doubleSpinBox_timeout.setMaximum(10.000000000000000)
        self.doubleSpinBox_timeout.setSingleStep(0.500000000000000)
        self.doubleSpinBox_timeout.setValue(1.500000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_timeout, 5, 1, 1, 1)

        self.labHost = QLabel(self.groupBox_speedTest)
        self.labHost.setObjectName(u"labHost")
        sizePolicy.setHeightForWidth(self.labHost.sizePolicy().hasHeightForWidth())
        self.labHost.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.labHost, 0, 0, 1, 1)

        self.templateEdit = QLineEdit(self.groupBox_speedTest)
        self.templateEdit.setObjectName(u"templateEdit")

        self.gridLayout_2.addWidget(self.templateEdit, 2, 1, 1, 1)

        self.spinBox_repeat = QSpinBox(self.groupBox_speedTest)
        self.spinBox_repeat.setObjectName(u"spinBox_repeat")
        sizePolicy2.setHeightForWidth(self.spinBox_repeat.sizePolicy().hasHeightForWidth())
        self.spinBox_repeat.setSizePolicy(sizePolicy2)
        self.spinBox_repeat.setMinimum(1)
        self.spinBox_repeat.setMaximum(10)
        self.spinBox_repeat.setValue(3)

        self.gridLayout_2.addWidget(self.spinBox_repeat, 7, 1, 1, 1)

        self.labThreads = QLabel(self.groupBox_speedTest)
        self.labThreads.setObjectName(u"labThreads")
        sizePolicy.setHeightForWidth(self.labThreads.sizePolicy().hasHeightForWidth())
        self.labThreads.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.labThreads, 3, 0, 1, 1)

        self.hostEdit = QLineEdit(self.groupBox_speedTest)
        self.hostEdit.setObjectName(u"hostEdit")

        self.gridLayout_2.addWidget(self.hostEdit, 0, 1, 1, 1)

        self.spinBox_workers = QSpinBox(self.groupBox_speedTest)
        self.spinBox_workers.setObjectName(u"spinBox_workers")
        sizePolicy2.setHeightForWidth(self.spinBox_workers.sizePolicy().hasHeightForWidth())
        self.spinBox_workers.setSizePolicy(sizePolicy2)
        self.spinBox_workers.setMinimum(1)
        self.spinBox_workers.setMaximum(256)
        self.spinBox_workers.setValue(64)

        self.gridLayout_2.addWidget(self.spinBox_workers, 3, 1, 1, 1)

        self.labTimeout = QLabel(self.groupBox_speedTest)
        self.labTimeout.setObjectName(u"labTimeout")
        sizePolicy.setHeightForWidth(self.labTimeout.sizePolicy().hasHeightForWidth())
        self.labTimeout.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.labTimeout, 5, 0, 1, 1)

        self.labTemplate = QLabel(self.groupBox_speedTest)
        self.labTemplate.setObjectName(u"labTemplate")
        sizePolicy.setHeightForWidth(self.labTemplate.sizePolicy().hasHeightForWidth())
        self.labTemplate.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.labTemplate, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_speedTest)

        self.groupBox_saveHosts = QGroupBox(Dialog)
        self.groupBox_saveHosts.setObjectName(u"groupBox_saveHosts")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_saveHosts)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAddHost = QPushButton(self.groupBox_saveHosts)
        self.btnAddHost.setObjectName(u"btnAddHost")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnAddHost.sizePolicy().hasHeightForWidth())
        self.btnAddHost.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.btnAddHost)

        self.btnRemoveHost = QPushButton(self.groupBox_saveHosts)
        self.btnRemoveHost.setObjectName(u"btnRemoveHost")
        sizePolicy3.setHeightForWidth(self.btnRemoveHost.sizePolicy().hasHeightForWidth())
        self.btnRemoveHost.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.btnRemoveHost)

        self.hostsEditSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.hostsEditSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.saveHostsList = QListWidget(self.groupBox_saveHosts)
        self.saveHostsList.setObjectName(u"saveHostsList")
        self.saveHostsList.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_2.addWidget(self.saveHostsList)


        self.verticalLayout.addWidget(self.groupBox_saveHosts)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnRestoreDefaults = QPushButton(Dialog)
        self.btnRestoreDefaults.setObjectName(u"btnRestoreDefaults")

        self.horizontalLayout.addWidget(self.btnRestoreDefaults)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u8bbe\u7f6e", None))
        self.groupBox_appearance.setTitle(QCoreApplication.translate("Dialog", u"\u5916\u89c2", None))
        self.labStyle.setText(QCoreApplication.translate("Dialog", u"\u4e3b\u9898", None))
        self.labGlobalFont.setText(QCoreApplication.translate("Dialog", u"\u5168\u5c40\u5b57\u4f53", None))
        self.labLanguage.setText(QCoreApplication.translate("Dialog", u"\u8bed\u8a00", None))
        self.comboBox_language.setItemText(0, QCoreApplication.translate("Dialog", u"\u4e2d\u6587", None))
        self.comboBox_language.setItemText(1, QCoreApplication.translate("Dialog", u"English", None))

        self.groupBox_speedTest.setTitle(QCoreApplication.translate("Dialog", u"\u6d4b\u901f", None))
        self.labRepeat.setText(QCoreApplication.translate("Dialog", u"\u6d4b\u8bd5\u6b21\u6570", None))
        self.labHost.setText(QCoreApplication.translate("Dialog", u"\u57df\u540d", None))
        self.templateEdit.setText(QCoreApplication.translate("Dialog", u"https://{}/translate_a/single?client=gtx&sl=en&tl=fr&q=a", None))
        self.templateEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u7528{}\u4ee3\u66ff\u57df\u540d", None))
        self.labThreads.setText(QCoreApplication.translate("Dialog", u"\u5e76\u53d1\u6570", None))
        self.hostEdit.setText(QCoreApplication.translate("Dialog", u"translate.googleapis.com", None))
        self.hostEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"translate.googleapis.com", None))
        self.labTimeout.setText(QCoreApplication.translate("Dialog", u"\u6d4b\u901f\u8d85\u65f6\uff08\u79d2\uff09", None))
        self.labTemplate.setText(QCoreApplication.translate("Dialog", u"\u8bf7\u6c42\u6a21\u677f", None))
        self.groupBox_saveHosts.setTitle(QCoreApplication.translate("Dialog", u"Hosts \u5199\u5165", None))
        self.btnAddHost.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0", None))
        self.btnRemoveHost.setText(QCoreApplication.translate("Dialog", u"\u5220\u9664", None))
        self.btnRestoreDefaults.setText(QCoreApplication.translate("Dialog", u"\u6062\u590d\u9ed8\u8ba4", None))
    # retranslateUi

