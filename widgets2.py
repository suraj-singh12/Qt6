import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setMinimumSize(QSize(350,200))


app = QApplication(sys.argv)
w = MainWindow()
w.show()

app.exec()