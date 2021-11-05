import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtGui import QPalette, QColor


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("My App")

        # creating tab like interface
        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)
        # layouts setting successful

        # button1: red
        btn = QPushButton("red")
        btn.pressed.connect(self.activate_tab_1)
        # add this button in button_layout(QHBoxLayout)
        button_layout.addWidget(btn)
        # add a widget(red color) to QStackLayout
        self.stacklayout.addWidget(Color("red"))

        # button2: green
        btn = QPushButton("green")
        btn.pressed.connect(self.activate_tab_2)
        # add this button in button_layout(QHBoxLayout)
        button_layout.addWidget(btn)
        # add a widget(green color) to QStackLayout
        self.stacklayout.addWidget(Color("green"))

        # button3: blue
        btn = QPushButton("blue")
        btn.pressed.connect(self.activate_tab_3)
        # add this button to button_layout(QHBoxLayout)
        button_layout.addWidget(btn)
        # add a widget(blue color) to QStackLayout
        self.stacklayout.addWidget(Color("blue"))

        widget = QWidget()
        widget.setLayout(pagelayout)

        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)


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
