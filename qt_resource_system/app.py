import sys
from PyQt5 import QtGui, QtWidgets
# compile the .qrc file using below command, and then
# import the compiled python module generated as a result
# pyrcc5 resources.qrc -o resources.py
import resources


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("resource testing")
        self.button = QtWidgets.QPushButton("My button")

        # resource name (:/virtual-folder-name/alias-name)
        icon = QtGui.QIcon(":/icons/penguin.png")
        self.button.setIcon(icon)
        self.button.clicked.connect(self.change_icon)

        self.setCentralWidget(self.button)

        self.show()

    def change_icon(self):
        icon = QtGui.QIcon(":/icons/monkey.png")
        self.button.setIcon(icon)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()