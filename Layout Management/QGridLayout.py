import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        self.setMinimumSize(QSize(400, 300))

        # QGridLayout widgets arranged in a grid
        # if you try using QVBoxLayout and QHBoxLayout for laying out multiple elements,
        # e.g. for a form, you’ll find it very difficult to ensure differently sized
        # widgets line up. The solution to this is QGridLayout.
        # You specify row and column positions for each widget.
        # You can skip elements, and they will be left empty.
        layout = QGridLayout()

        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('blue'), 1, 0)
        layout.addWidget(Color('green'), 1, 1)
        layout.addWidget(Color('lightgreen'), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()