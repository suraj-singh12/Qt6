import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("My App")

        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QVBoxLayout()

        # You can set the spacing around the layout using .setContentMargins or
        layout1.setContentsMargins(0, 0, 0, 0)
        # set the spacing between elements using .setSpacing.
        layout1.setSpacing(10)

        layout2.setContentsMargins(15, 15, 20, 15)

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        layout1.addLayout(layout2)
        # so first all widget of layout2 will come

        layout1.addWidget(Color('green'))
        # now the widgets of layout1 will appear after layout2

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))

        layout1.addLayout(layout3)
        # now one more section will be made (last) where widgets of layout3 will appear

        widget = QWidget()
        widget.setLayout(layout1)

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