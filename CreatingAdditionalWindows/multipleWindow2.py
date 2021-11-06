import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from random import randint


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent,
    it will appear as a free-floating window.
    """

    def __init__(self):
        super(AnotherWindow, self).__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window %d" % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class LogWindow(QWidget):
    def __init__(self):
        super(LogWindow, self).__init__()
        self.setWindowTitle("Log Window")
        self.setMinimumSize(QSize(350,  100))
        self.label = QLabel("All Program logs will appear here.")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
        self.setMinimumSize(QSize(300, 200))
        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()

        self.window3 = LogWindow()
        self.window3.show()
        self.window4 = LogWindow()
        self.window4.show()

        l = QVBoxLayout()
        button1 = QPushButton("Push for window 1")
        button1.clicked.connect(self.toggle_window1)
        l.addWidget(button1)

        button2 = QPushButton("Push for window 2")
        button2.clicked.connect(self.toggle_window2)
        l.addWidget(button2)

        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

    def toggle_window1(self, checked):
        if self.window1.isVisible():
            self.window1.hide()
        else:
            self.window1.show()

    def toggle_window2(self, checked):
        if self.window2.isVisible():
            self.window2.hide()
        else:
            self.window2.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
