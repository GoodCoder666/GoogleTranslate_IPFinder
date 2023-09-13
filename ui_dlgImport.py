# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlgImport.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGroupBox, QHBoxLayout, QLineEdit,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(266, 326)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_Mode = QGroupBox(Dialog)
        self.groupBox_Mode.setObjectName(u"groupBox_Mode")
        self.horizontalLayout = QHBoxLayout(self.groupBox_Mode)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioAppend = QRadioButton(self.groupBox_Mode)
        self.radioAppend.setObjectName(u"radioAppend")
        self.radioAppend.setChecked(True)

        self.horizontalLayout.addWidget(self.radioAppend)

        self.radioReplace = QRadioButton(self.groupBox_Mode)
        self.radioReplace.setObjectName(u"radioReplace")

        self.horizontalLayout.addWidget(self.radioReplace)


        self.verticalLayout.addWidget(self.groupBox_Mode)

        self.groupBox_Source = QGroupBox(Dialog)
        self.groupBox_Source.setObjectName(u"groupBox_Source")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_Source.sizePolicy().hasHeightForWidth())
        self.groupBox_Source.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_Source)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.radioLocalFile = QRadioButton(self.groupBox_Source)
        self.radioLocalFile.setObjectName(u"radioLocalFile")

        self.verticalLayout_3.addWidget(self.radioLocalFile)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioSingleIP = QRadioButton(self.groupBox_Source)
        self.radioSingleIP.setObjectName(u"radioSingleIP")

        self.horizontalLayout_2.addWidget(self.radioSingleIP)

        self.singleIPEdit = QLineEdit(self.groupBox_Source)
        self.singleIPEdit.setObjectName(u"singleIPEdit")
        self.singleIPEdit.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.singleIPEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.radioOnline = QRadioButton(self.groupBox_Source)
        self.radioOnline.setObjectName(u"radioOnline")
        self.radioOnline.setChecked(True)

        self.verticalLayout_3.addWidget(self.radioOnline)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, -1, -1, -1)
        self.chkBox_std4 = QCheckBox(self.groupBox_Source)
        self.chkBox_std4.setObjectName(u"chkBox_std4")
        self.chkBox_std4.setChecked(True)

        self.verticalLayout_2.addWidget(self.chkBox_std4)

        self.chkBox_ext4 = QCheckBox(self.groupBox_Source)
        self.chkBox_ext4.setObjectName(u"chkBox_ext4")

        self.verticalLayout_2.addWidget(self.chkBox_ext4)

        self.chkBox_std6 = QCheckBox(self.groupBox_Source)
        self.chkBox_std6.setObjectName(u"chkBox_std6")

        self.verticalLayout_2.addWidget(self.chkBox_std6)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioCustomURL = QRadioButton(self.groupBox_Source)
        self.radioCustomURL.setObjectName(u"radioCustomURL")

        self.horizontalLayout_3.addWidget(self.radioCustomURL)

        self.customURLEdit = QLineEdit(self.groupBox_Source)
        self.customURLEdit.setObjectName(u"customURLEdit")
        self.customURLEdit.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.customURLEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.groupBox_Source)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.radioOnline.toggled.connect(self.chkBox_std4.setEnabled)
        self.radioOnline.toggled.connect(self.chkBox_ext4.setEnabled)
        self.radioOnline.toggled.connect(self.chkBox_std6.setEnabled)
        self.radioSingleIP.toggled.connect(self.singleIPEdit.setEnabled)
        self.radioCustomURL.toggled.connect(self.customURLEdit.setEnabled)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5bfc\u5165\u9009\u9879", None))
        self.groupBox_Mode.setTitle(QCoreApplication.translate("Dialog", u"\u5bfc\u5165\u6a21\u5f0f", None))
        self.radioAppend.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u5e76\u53bb\u91cd", None))
        self.radioReplace.setText(QCoreApplication.translate("Dialog", u"\u66ff\u6362\u5168\u90e8", None))
        self.groupBox_Source.setTitle(QCoreApplication.translate("Dialog", u"\u5bfc\u5165\u6765\u6e90", None))
        self.radioLocalFile.setText(QCoreApplication.translate("Dialog", u"\u672c\u5730\u6587\u4ef6", None))
        self.radioSingleIP.setText(QCoreApplication.translate("Dialog", u"\u5355\u4e2a IP\uff1a", None))
        self.radioOnline.setText(QCoreApplication.translate("Dialog", u"\u5728\u7ebf\u670d\u52a1\uff1a", None))
        self.chkBox_std4.setText(QCoreApplication.translate("Dialog", u"\u7cbe\u7b80 IPv4", None))
        self.chkBox_ext4.setText(QCoreApplication.translate("Dialog", u"\u6269\u5c55 IPv4", None))
        self.chkBox_std6.setText(QCoreApplication.translate("Dialog", u"\u6807\u51c6 IPv6", None))
        self.radioCustomURL.setText(QCoreApplication.translate("Dialog", u"\u81ea\u5b9a\u4e49 URL\uff1a", None))
    # retranslateUi

