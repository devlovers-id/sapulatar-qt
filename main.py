# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QWidget, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

if __name__ == "__main__":
    loader = QUiLoader()
    app = QApplication(sys.argv)
    main_window = loader.load("form.ui", None)
    main_window.show()
    app.exec_()
