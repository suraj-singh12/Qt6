import sys
from PyQt5 import QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("resource testing")
        self.button = QtWidgets.QPushButton("My button")

        icon = QtGui.QIcon("animal-penguin.png")
        self.button.setIcon(icon)
        self.button.clicked.connect(self.change_icon)

        self.setCentralWidget(self.button)

        self.show()

    def change_icon(self):
        icon = QtGui.QIcon("animal-monkey.png")
        self.button.setIcon(icon)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()