# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlgDebug.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(544, 265)
        self.horizontalLayout_6 = QHBoxLayout(Dialog)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_network = QGroupBox(Dialog)
        self.groupBox_network.setObjectName(u"groupBox_network")
        self.verticalLayout = QVBoxLayout(self.groupBox_network)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labIP = QLabel(self.groupBox_network)
        self.labIP.setObjectName(u"labIP")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labIP.sizePolicy().hasHeightForWidth())
        self.labIP.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.labIP)

        self.ipEdit = QLineEdit(self.groupBox_network)
        self.ipEdit.setObjectName(u"ipEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ipEdit.sizePolicy().hasHeightForWidth())
        self.ipEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.ipEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labHost = QLabel(self.groupBox_network)
        self.labHost.setObjectName(u"labHost")
        sizePolicy.setHeightForWidth(self.labHost.sizePolicy().hasHeightForWidth())
        self.labHost.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.labHost)

        self.hostEdit = QLineEdit(self.groupBox_network)
        self.hostEdit.setObjectName(u"hostEdit")
        sizePolicy1.setHeightForWidth(self.hostEdit.sizePolicy().hasHeightForWidth())
        self.hostEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.hostEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labFormat = QLabel(self.groupBox_network)
        self.labFormat.setObjectName(u"labFormat")
        sizePolicy.setHeightForWidth(self.labFormat.sizePolicy().hasHeightForWidth())
        self.labFormat.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.labFormat)

        self.formatEdit = QLineEdit(self.groupBox_network)
        self.formatEdit.setObjectName(u"formatEdit")
        sizePolicy1.setHeightForWidth(self.formatEdit.sizePolicy().hasHeightForWidth())
        self.formatEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.formatEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.groupBox_network)

        self.groupBox_debug = QGroupBox(Dialog)
        self.groupBox_debug.setObjectName(u"groupBox_debug")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_debug)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labTimeout = QLabel(self.groupBox_debug)
        self.labTimeout.setObjectName(u"labTimeout")
        sizePolicy.setHeightForWidth(self.labTimeout.sizePolicy().hasHeightForWidth())
        self.labTimeout.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.labTimeout)

        self.spinBox_timeout = QDoubleSpinBox(self.groupBox_debug)
        self.spinBox_timeout.setObjectName(u"spinBox_timeout")
        sizePolicy1.setHeightForWidth(self.spinBox_timeout.sizePolicy().hasHeightForWidth())
        self.spinBox_timeout.setSizePolicy(sizePolicy1)
        self.spinBox_timeout.setMinimum(1.000000000000000)
        self.spinBox_timeout.setMaximum(10.000000000000000)
        self.spinBox_timeout.setSingleStep(0.500000000000000)
        self.spinBox_timeout.setValue(2.500000000000000)

        self.horizontalLayout_2.addWidget(self.spinBox_timeout)

        self.labTimeoutUnit = QLabel(self.groupBox_debug)
        self.labTimeoutUnit.setObjectName(u"labTimeoutUnit")
        sizePolicy.setHeightForWidth(self.labTimeoutUnit.sizePolicy().hasHeightForWidth())
        self.labTimeoutUnit.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.labTimeoutUnit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labTimes = QLabel(self.groupBox_debug)
        self.labTimes.setObjectName(u"labTimes")
        sizePolicy.setHeightForWidth(self.labTimes.sizePolicy().hasHeightForWidth())
        self.labTimes.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.labTimes)

        self.spinBox_times = QSpinBox(self.groupBox_debug)
        self.spinBox_times.setObjectName(u"spinBox_times")
        sizePolicy1.setHeightForWidth(self.spinBox_times.sizePolicy().hasHeightForWidth())
        self.spinBox_times.setSizePolicy(sizePolicy1)
        self.spinBox_times.setMinimum(1)
        self.spinBox_times.setMaximum(20)

        self.horizontalLayout.addWidget(self.spinBox_times)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.groupBox_debug)

        self.btnDebug = QPushButton(Dialog)
        self.btnDebug.setObjectName(u"btnDebug")

        self.verticalLayout_2.addWidget(self.btnDebug)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_6.addWidget(self.textBrowser)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u8c03\u8bd5", None))
        self.groupBox_network.setTitle(QCoreApplication.translate("Dialog", u"\u7f51\u7edc\u53c2\u6570", None))
        self.labIP.setText(QCoreApplication.translate("Dialog", u"IP\uff1a", None))
        self.labHost.setText(QCoreApplication.translate("Dialog", u"\u4e3b\u673a\uff1a", None))
        self.labFormat.setText(QCoreApplication.translate("Dialog", u"\u8bf7\u6c42\u6a21\u677f\uff1a", None))
        self.groupBox_debug.setTitle(QCoreApplication.translate("Dialog", u"\u8c03\u8bd5\u53c2\u6570", None))
        self.labTimeout.setText(QCoreApplication.translate("Dialog", u"\u54cd\u5e94\u65f6\u95f4\u4e0a\u9650\uff1a", None))
        self.labTimeoutUnit.setText(QCoreApplication.translate("Dialog", u"s", None))
        self.labTimes.setText(QCoreApplication.translate("Dialog", u"\u8c03\u8bd5\u6b21\u6570\uff1a", None))
        self.btnDebug.setText(QCoreApplication.translate("Dialog", u"\u8c03\u8bd5", None))
    # retranslateUi

