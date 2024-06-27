# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlgAbout.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QDialog, QGridLayout,
    QGroupBox, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(501, 353)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_repo = QGroupBox(Dialog)
        self.groupBox_repo.setObjectName(u"groupBox_repo")
        self.gridLayout_2 = QGridLayout(self.groupBox_repo)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.githubLink = QCommandLinkButton(self.groupBox_repo)
        self.githubLink.setObjectName(u"githubLink")

        self.gridLayout_2.addWidget(self.githubLink, 0, 1, 1, 1)

        self.gtdbLink = QCommandLinkButton(self.groupBox_repo)
        self.gtdbLink.setObjectName(u"gtdbLink")

        self.gridLayout_2.addWidget(self.gtdbLink, 0, 2, 1, 1)

        self.licenseLink = QCommandLinkButton(self.groupBox_repo)
        self.licenseLink.setObjectName(u"licenseLink")

        self.gridLayout_2.addWidget(self.licenseLink, 1, 1, 1, 1)

        self.readmeLink = QCommandLinkButton(self.groupBox_repo)
        self.readmeLink.setObjectName(u"readmeLink")

        self.gridLayout_2.addWidget(self.readmeLink, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_repo, 0, 0, 1, 2)

        self.btnUpdate = QPushButton(Dialog)
        self.btnUpdate.setObjectName(u"btnUpdate")

        self.gridLayout.addWidget(self.btnUpdate, 3, 1, 1, 1)

        self.labCopyright = QLabel(Dialog)
        self.labCopyright.setObjectName(u"labCopyright")

        self.gridLayout.addWidget(self.labCopyright, 3, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.RichText)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setOpenExternalLinks(True)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5173\u4e8e", None))
        self.groupBox_repo.setTitle(QCoreApplication.translate("Dialog", u"\u4ee3\u7801\u4ed3\u5e93", None))
        self.githubLink.setText(QCoreApplication.translate("Dialog", u"GitHub \u9879\u76ee\u5730\u5740", None))
        self.githubLink.setDescription(QCoreApplication.translate("Dialog", u"https://github.com/GoodCoder666/GoogleTranslate_IPFinder", None))
        self.gtdbLink.setText(QCoreApplication.translate("Dialog", u"\u5b98\u65b9 IP \u5e93", None))
        self.gtdbLink.setDescription(QCoreApplication.translate("Dialog", u"https://github.com/GoodCoder666/gtdb", None))
        self.licenseLink.setText(QCoreApplication.translate("Dialog", u"\u7248\u6743\u6761\u6b3e\uff08GPLv3\uff09", None))
        self.licenseLink.setDescription(QCoreApplication.translate("Dialog", u"https://github.com/GoodCoder666/GoogleTranslate_IPFinder/blob/main/LICENSE", None))
        self.readmeLink.setText(QCoreApplication.translate("Dialog", u"README \u5e2e\u52a9\u6587\u4ef6", None))
        self.readmeLink.setDescription(QCoreApplication.translate("Dialog", u"https://github.com/GoodCoder666/GoogleTranslate_IPFinder/blob/main/README.md", None))
        self.btnUpdate.setText(QCoreApplication.translate("Dialog", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.labCopyright.setText(QCoreApplication.translate("Dialog", u"Copyright \u00a9 GoodCoder666 2024", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u611f\u8c22\u4f7f\u7528<span style=\" font-weight:700;\"> GoogleTranslate_IPFinder</span>\uff01\u6b22\u8fce\u5728 <a href=\"https://github.com/GoodCoder666/GoogleTranslate_IPFinder/issues\"><span style=\" text-decoration: underline; color:#0000ff;\">issues</span></a> \u6307\u51fa bug \u6216\u63d0\u51fa\u4fee\u6539\u610f\u89c1\u3002 </p><p>\u5728 <a href=\"https://github.com/GoodCoder666/GoogleTranslate_IPFinder\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub</span></a> \u4e0a Star \u6b64\u9879\u76ee\uff1a<a href=\"https://github.com/GoodCoder666/GoogleTranslate_IPFinder\"><span style=\" text-decoration: underline; color:#0000ff;\">GoodCoder666/GoogleTranslate_IPFinder</span></a></p></body></html>", None))
    # retranslateUi

