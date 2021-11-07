# Two ways to load a .ui file:
# 1. load into a class using uic.loadUi() of PyQt5
# 2. convert it to python using pyuic5 tool

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

app = QApplication(sys.argv)

window = uic.loadUi("mainwindow.ui")
window.show()
app.exec()
