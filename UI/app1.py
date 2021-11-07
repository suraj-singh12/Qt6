import sys
from PyQt5 import QtWidgets, uic

from MainWindow import Ui_MainWindow
# NOTE: the Ui_MainWindow code was created via below command:
# pyuic5 mainwindow.ui -o MainWindow.py


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
