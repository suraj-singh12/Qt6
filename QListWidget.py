import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("My App")

        # This widget is similar to QComboBox, except options are presented
        # as a scrollable list of items. It also supports selection of multiple
        # items at once.
        widget = QListWidget()
        widget.addItems(["one", "two", "three"])

        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i.text())

    def text_changed(self, s):
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()