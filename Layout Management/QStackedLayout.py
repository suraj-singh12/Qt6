import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setMinimumSize(QSize(400,300))
        self.setWindowTitle("My App")

        # QStackedLayout: multiple widgets in the same space. select which widget to show.
        # Use: drawing layers in a graphic application, or for imitating a tab-like interface.
        # QStackedWidget: a container widget works exactly like QStackLayout
        # useful if want to add a stack directly to a QMainWindow with .setCentralWidget.
        layout = QStackedLayout()

        layout.addWidget(Color('red'))
        layout.addWidget(Color('blue'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('yellow'))

        # widget at index 2 will be visible
        layout.setCurrentIndex(2)

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