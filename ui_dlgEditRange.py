# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlgEditRange.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGroupBox, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(370, 412)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_edit = QGroupBox(Dialog)
        self.groupBox_edit.setObjectName(u"groupBox_edit")
        self.horizontalLayout = QHBoxLayout(self.groupBox_edit)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnAdd = QPushButton(self.groupBox_edit)
        self.btnAdd.setObjectName(u"btnAdd")

        self.horizontalLayout.addWidget(self.btnAdd)

        self.btnRemove = QPushButton(self.groupBox_edit)
        self.btnRemove.setObjectName(u"btnRemove")

        self.horizontalLayout.addWidget(self.btnRemove)

        self.btnReset = QPushButton(self.groupBox_edit)
        self.btnReset.setObjectName(u"btnReset")

        self.horizontalLayout.addWidget(self.btnReset)

        self.btnClear = QPushButton(self.groupBox_edit)
        self.btnClear.setObjectName(u"btnClear")

        self.horizontalLayout.addWidget(self.btnClear)


        self.verticalLayout.addWidget(self.groupBox_edit)

        self.rangesTable = QTableWidget(Dialog)
        if (self.rangesTable.columnCount() < 2):
            self.rangesTable.setColumnCount(2)
        self.rangesTable.setObjectName(u"rangesTable")
        self.rangesTable.setShowGrid(False)
        self.rangesTable.setColumnCount(2)

        self.verticalLayout.addWidget(self.rangesTable)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u7f16\u8f91 IP \u6bb5", None))
        self.groupBox_edit.setTitle(QCoreApplication.translate("Dialog", u"\u7f16\u8f91", None))
        self.btnAdd.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0", None))
        self.btnRemove.setText(QCoreApplication.translate("Dialog", u"\u5220\u9664", None))
        self.btnReset.setText(QCoreApplication.translate("Dialog", u"\u91cd\u7f6e", None))
        self.btnClear.setText(QCoreApplication.translate("Dialog", u"\u6e05\u7a7a", None))
    # retranslateUi

