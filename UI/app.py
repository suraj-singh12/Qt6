# Two ways to load a .ui file:
# 1. load into a class using uic.loadUi() of PyQt5
# 2. convert it to python using pyuic5 tool

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # loading UI from the __init__() block of existing widget(here QMainWindow)
        uic.loadUi("mainwindow.ui", self)


app = QApplication(sys.argv)
window = MainWindow()
# As the uic.loadUi() method turns an instance object we cannot attach custom
# __init__() code. However, we can handle this through a custom setup function.
window.show()
app.exec()
