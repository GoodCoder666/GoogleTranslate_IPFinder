# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u":/images/icons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labIP = QLabel(self.centralwidget)
        self.labIP.setObjectName(u"labIP")

        self.horizontalLayout.addWidget(self.labIP)

        self.btnWait_Scan = QPushButton(self.centralwidget)
        self.btnWait_Scan.setObjectName(u"btnWait_Scan")

        self.horizontalLayout.addWidget(self.btnWait_Scan)

        self.btnWait_Load = QPushButton(self.centralwidget)
        self.btnWait_Load.setObjectName(u"btnWait_Load")

        self.horizontalLayout.addWidget(self.btnWait_Load)

        self.btnWait_Test = QPushButton(self.centralwidget)
        self.btnWait_Test.setObjectName(u"btnWait_Test")

        self.horizontalLayout.addWidget(self.btnWait_Test)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.ipList = QListWidget(self.centralwidget)
        self.ipList.setObjectName(u"ipList")

        self.verticalLayout.addWidget(self.ipList)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labTestResult = QLabel(self.centralwidget)
        self.labTestResult.setObjectName(u"labTestResult")

        self.horizontalLayout_2.addWidget(self.labTestResult)

        self.btnResult_Save = QPushButton(self.centralwidget)
        self.btnResult_Save.setObjectName(u"btnResult_Save")

        self.horizontalLayout_2.addWidget(self.btnResult_Save)

        self.btnResult_Copy = QPushButton(self.centralwidget)
        self.btnResult_Copy.setObjectName(u"btnResult_Copy")

        self.horizontalLayout_2.addWidget(self.btnResult_Copy)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.resultTable = QTableWidget(self.centralwidget)
        if (self.resultTable.columnCount() < 2):
            self.resultTable.setColumnCount(2)
        self.resultTable.setObjectName(u"resultTable")
        self.resultTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.resultTable.setSortingEnabled(True)
        self.resultTable.setColumnCount(2)

        self.verticalLayout_2.addWidget(self.resultTable)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8c37\u6b4c\u7ffb\u8bd1IP\u6d4b\u901f\u5de5\u5177", None))
        self.labIP.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u6d4b\u901f\u7684IP\uff1a", None))
        self.btnWait_Scan.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf", None))
        self.btnWait_Load.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
        self.btnWait_Test.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u901f", None))
        self.labTestResult.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u901f\u7ed3\u679c\uff1a", None))
        self.btnResult_Save.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.btnResult_Copy.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236", None))
    # retranslateUi

