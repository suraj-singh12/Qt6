import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import randint


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super(AnotherWindow, self).__init__()
        self.label = QLabel("Another Window %d" % randint(0, 100))

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        self.w = None           # signifying no external window yet

        self.button = QPushButton("Push for window")
        self.button.clicked.connect(self.show_new_window)

        self.setCentralWidget(self.button)

    # everytime we click the button, a new window is created.
    # but what if we don't want to create a new window?
    # we will check if window does not exist then create
    def show_new_window(self, checked):
        # now even after control goes out of fn, the window is alive
        # because it is not in a local fn variable like before now

        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()
        else:
            self.w.close()      # close the window
            self.w = None       # Discard reference
        # if we do not use self.w.close() then if the window has any other reference,
        # then it will not close, so we explicitly ensure it closes


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
