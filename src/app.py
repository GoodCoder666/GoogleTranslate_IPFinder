import sys
from PySide6.QtWidgets import QApplication
from src.ui.mainWindow import MainWindow

def run_app():
    app = QApplication(sys.argv)
    mainform = MainWindow()
    mainform.show()
    sys.exit(app.exec())
