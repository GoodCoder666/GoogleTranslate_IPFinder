# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlgScan.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QDoubleSpinBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(228, 187)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.maxIPLayout = QHBoxLayout()
        self.maxIPLayout.setObjectName(u"maxIPLayout")
        self.labMaxIP_1 = QLabel(Dialog)
        self.labMaxIP_1.setObjectName(u"labMaxIP_1")

        self.maxIPLayout.addWidget(self.labMaxIP_1)

        self.spinBox_MaxIP = QSpinBox(Dialog)
        self.spinBox_MaxIP.setObjectName(u"spinBox_MaxIP")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_MaxIP.sizePolicy().hasHeightForWidth())
        self.spinBox_MaxIP.setSizePolicy(sizePolicy)
        self.spinBox_MaxIP.setMinimum(1)
        self.spinBox_MaxIP.setMaximum(1000)
        self.spinBox_MaxIP.setValue(35)

        self.maxIPLayout.addWidget(self.spinBox_MaxIP)

        self.labMaxIP_2 = QLabel(Dialog)
        self.labMaxIP_2.setObjectName(u"labMaxIP_2")

        self.maxIPLayout.addWidget(self.labMaxIP_2)


        self.verticalLayout.addLayout(self.maxIPLayout)

        self.threadsLayout = QHBoxLayout()
        self.threadsLayout.setObjectName(u"threadsLayout")
        self.labThreads = QLabel(Dialog)
        self.labThreads.setObjectName(u"labThreads")

        self.threadsLayout.addWidget(self.labThreads)

        self.comboBox_threads = QComboBox(Dialog)
        self.comboBox_threads.addItem("")
        self.comboBox_threads.addItem("")
        self.comboBox_threads.addItem("")
        self.comboBox_threads.addItem("")
        self.comboBox_threads.addItem("")
        self.comboBox_threads.addItem("")
        self.comboBox_threads.addItem("")
        self.comboBox_threads.addItem("")
        self.comboBox_threads.addItem("")
        self.comboBox_threads.setObjectName(u"comboBox_threads")
        sizePolicy.setHeightForWidth(self.comboBox_threads.sizePolicy().hasHeightForWidth())
        self.comboBox_threads.setSizePolicy(sizePolicy)

        self.threadsLayout.addWidget(self.comboBox_threads)


        self.verticalLayout.addLayout(self.threadsLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labTimeout = QLabel(Dialog)
        self.labTimeout.setObjectName(u"labTimeout")

        self.horizontalLayout.addWidget(self.labTimeout)

        self.spinBox_timeout = QDoubleSpinBox(Dialog)
        self.spinBox_timeout.setObjectName(u"spinBox_timeout")
        sizePolicy.setHeightForWidth(self.spinBox_timeout.sizePolicy().hasHeightForWidth())
        self.spinBox_timeout.setSizePolicy(sizePolicy)
        self.spinBox_timeout.setMinimum(1.000000000000000)
        self.spinBox_timeout.setMaximum(10.000000000000000)
        self.spinBox_timeout.setSingleStep(0.500000000000000)
        self.spinBox_timeout.setValue(1.500000000000000)

        self.horizontalLayout.addWidget(self.spinBox_timeout)

        self.labTimeout_2 = QLabel(Dialog)
        self.labTimeout_2.setObjectName(u"labTimeout_2")

        self.horizontalLayout.addWidget(self.labTimeout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labScanRanges = QLabel(Dialog)
        self.labScanRanges.setObjectName(u"labScanRanges")

        self.horizontalLayout_2.addWidget(self.labScanRanges)

        self.btnEditRanges = QPushButton(Dialog)
        self.btnEditRanges.setObjectName(u"btnEditRanges")

        self.horizontalLayout_2.addWidget(self.btnEditRanges)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.chkBoxLayout = QHBoxLayout()
        self.chkBoxLayout.setObjectName(u"chkBoxLayout")
        self.chkBox_randomizeScan = QCheckBox(Dialog)
        self.chkBox_randomizeScan.setObjectName(u"chkBox_randomizeScan")

        self.chkBoxLayout.addWidget(self.chkBox_randomizeScan)

        self.chkBox_autoTest = QCheckBox(Dialog)
        self.chkBox_autoTest.setObjectName(u"chkBox_autoTest")
        self.chkBox_autoTest.setChecked(True)

        self.chkBoxLayout.addWidget(self.chkBox_autoTest)


        self.verticalLayout.addLayout(self.chkBoxLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.comboBox_threads.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u626b\u63cf\u8bbe\u7f6e", None))
        self.labMaxIP_1.setText(QCoreApplication.translate("Dialog", u"\u626b\u63cf\u51fa", None))
        self.labMaxIP_2.setText(QCoreApplication.translate("Dialog", u"\u6761IP\u540e\u505c\u6b62\u626b\u63cf", None))
        self.labThreads.setText(QCoreApplication.translate("Dialog", u"\u6700\u5927\u7ebf\u7a0b\u6570\uff1a", None))
        self.comboBox_threads.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.comboBox_threads.setItemText(1, QCoreApplication.translate("Dialog", u"2", None))
        self.comboBox_threads.setItemText(2, QCoreApplication.translate("Dialog", u"4", None))
        self.comboBox_threads.setItemText(3, QCoreApplication.translate("Dialog", u"8", None))
        self.comboBox_threads.setItemText(4, QCoreApplication.translate("Dialog", u"16", None))
        self.comboBox_threads.setItemText(5, QCoreApplication.translate("Dialog", u"32", None))
        self.comboBox_threads.setItemText(6, QCoreApplication.translate("Dialog", u"64", None))
        self.comboBox_threads.setItemText(7, QCoreApplication.translate("Dialog", u"128", None))
        self.comboBox_threads.setItemText(8, QCoreApplication.translate("Dialog", u"200", None))

        self.labTimeout.setText(QCoreApplication.translate("Dialog", u"\u54cd\u5e94\u65f6\u95f4\u4e0a\u9650\uff1a", None))
        self.labTimeout_2.setText(QCoreApplication.translate("Dialog", u"s", None))
        self.labScanRanges.setText(QCoreApplication.translate("Dialog", u"\u626b\u63cf IP \u6bb5\uff1a", None))
        self.btnEditRanges.setText(QCoreApplication.translate("Dialog", u"\u7f16\u8f91...", None))
#if QT_CONFIG(tooltip)
        self.chkBox_randomizeScan.setToolTip(QCoreApplication.translate("Dialog", u"\u4ee5\u968f\u673a\u7684\u987a\u5e8f\u6267\u884c\u626b\u63cf\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.chkBox_randomizeScan.setText(QCoreApplication.translate("Dialog", u"\u968f\u673a\u5316\u626b\u63cf", None))
        self.chkBox_autoTest.setText(QCoreApplication.translate("Dialog", u"\u5b8c\u6210\u540e\u81ea\u52a8\u6d4b\u901f", None))
    # retranslateUi

