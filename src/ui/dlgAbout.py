# -*- coding: utf-8 -*-
from functools import partial

from PySide6.QtWidgets import QDialog

from src.core.utils import open_url
from src.ui.generated.ui_dlgAbout import Ui_Dialog

__all__ = ['dlgAbout']

class dlgAbout(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        for link in (self.ui.githubLink, self.ui.gtdbLink, self.ui.licenseLink, self.ui.readmeLink):
            link.clicked.connect(partial(open_url, link.description()))
        self.ui.btnUpdate.clicked.connect(partial(open_url, 'https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases/latest'))
