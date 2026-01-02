# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
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
        self.actSettings = QAction(MainWindow)
        self.actSettings.setObjectName(u"actSettings")
        self.actResetSettings = QAction(MainWindow)
        self.actResetSettings.setObjectName(u"actResetSettings")
        self.actProjectHomepage = QAction(MainWindow)
        self.actProjectHomepage.setObjectName(u"actProjectHomepage")
        self.actCheckUpdates = QAction(MainWindow)
        self.actCheckUpdates.setObjectName(u"actCheckUpdates")
        self.actAbout = QAction(MainWindow)
        self.actAbout.setObjectName(u"actAbout")
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

        self.btnWait_Import = QPushButton(self.centralwidget)
        self.btnWait_Import.setObjectName(u"btnWait_Import")

        self.horizontalLayout.addWidget(self.btnWait_Import)

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

        self.btnResult_WriteHosts = QPushButton(self.centralwidget)
        self.btnResult_WriteHosts.setObjectName(u"btnResult_WriteHosts")

        self.horizontalLayout_2.addWidget(self.btnResult_WriteHosts)


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
        self.optionsMenu = QMenu(self.menubar)
        self.optionsMenu.setObjectName(u"optionsMenu")
        self.helpMenu = QMenu(self.menubar)
        self.helpMenu.setObjectName(u"helpMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.optionsMenu.menuAction())
        self.menubar.addAction(self.helpMenu.menuAction())
        self.optionsMenu.addAction(self.actSettings)
        self.optionsMenu.addSeparator()
        self.optionsMenu.addAction(self.actResetSettings)
        self.helpMenu.addAction(self.actProjectHomepage)
        self.helpMenu.addAction(self.actCheckUpdates)
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.actAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8c37\u6b4c\u7ffb\u8bd1IP\u6d4b\u901f\u5de5\u5177", None))
        self.actSettings.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u2026", None))
#if QT_CONFIG(shortcut)
        self.actSettings.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+,", None))
#endif // QT_CONFIG(shortcut)
        self.actResetSettings.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e\u8bbe\u7f6e", None))
        self.actProjectHomepage.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u4e3b\u9875", None))
        self.actCheckUpdates.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.actAbout.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u2026", None))
#if QT_CONFIG(shortcut)
        self.actAbout.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
        self.labIP.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u6d4b\u901f\u7684IP\uff1a", None))
#if QT_CONFIG(tooltip)
        self.btnWait_Scan.setToolTip(QCoreApplication.translate("MainWindow", u"\u4ece\u8c37\u6b4c\u7684IP\u7f51\u7edc\u4e2d\u627e\u5230\u53ef\u7528\u7684IP\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.btnWait_Scan.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf", None))
#if QT_CONFIG(tooltip)
        self.btnWait_Import.setToolTip(QCoreApplication.translate("MainWindow", u"\u4ece\u6307\u5b9a\u6765\u6e90\u5bfc\u5165IP\u5217\u8868\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.btnWait_Import.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
#if QT_CONFIG(tooltip)
        self.btnWait_Test.setToolTip(QCoreApplication.translate("MainWindow", u"\u5bf9\u5217\u8868\u4e2d\u7684IP\u8fdb\u884c\u53ef\u7528\u6027\u6d4b\u8bd5\u5e76\u6309\u54cd\u5e94\u901f\u5ea6\u6392\u5e8f\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.btnWait_Test.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u901f", None))
        self.labTestResult.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u901f\u7ed3\u679c\uff1a", None))
#if QT_CONFIG(tooltip)
        self.btnResult_Save.setToolTip(QCoreApplication.translate("MainWindow", u"\u5c06\u6d4b\u901f\u7ed3\u679c\u5bfc\u51fa\u81f3\u6587\u4ef6\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.btnResult_Save.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
#if QT_CONFIG(tooltip)
        self.btnResult_Copy.setToolTip(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u6700\u5feb\u901f\u7684IP\u4ee5\u4fbf\u624b\u52a8\u5199\u5165Hosts\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.btnResult_Copy.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236", None))
#if QT_CONFIG(tooltip)
        self.btnResult_WriteHosts.setToolTip(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u5c06\u54cd\u5e94\u6700\u5feb\u7684IP\u5199\u5165Hosts\uff08\u9700\u8981\u7ba1\u7406\u5458\u6743\u9650\uff09\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.btnResult_WriteHosts.setText(QCoreApplication.translate("MainWindow", u"\u5199\u5165Hosts", None))
        self.optionsMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u9879", None))
        self.helpMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

