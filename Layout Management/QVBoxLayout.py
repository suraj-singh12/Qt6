import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("My App")

        # QVBoxLayout allows widgets to be arranged linearly one above other (vertically)
        # Adding a widget adds it to the bottom of the column
        layout = QVBoxLayout()      # creating layout (QVBoxLayout())

        # adding a widget in this layout (here just color basically)
        layout.addWidget(Color('lightgreen'))
        # the border now visible around the lightgreen widget is layout spacing

        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('blue'))
        # layout.addWidget(Color('green'))

        widget = QWidget()          # new simple Widget
        widget.setLayout(layout)    # adding our layout on this widget
        # Now the scene is:
        # We have QWidget() as the main(root) widget on QMainWindow
        # On this QWidget() we have our QVBoxLayout applied
        # In that QVBoxLayout we have our widgets (vertically one above other in linear fashion)

        self.setCentralWidget(widget)   # apply this simple widget with our layout to QMainWindow


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
