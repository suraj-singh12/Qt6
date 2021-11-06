import sys
from PyQt5.QtWidgets import *
from random import randint

# So far we've looked at how to create new windows on demand.
# However, sometimes you have a number of standard application windows.
# In this case rather than create the windows when you want to show them,
# it can often make more sense to create them at start-up,
# then use .show() to display them when needed.


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
        # creating our external window here itself (at startup of application)
        self.w = AnotherWindow()

        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        # showing our external window (after clicking push button)
        self.w.show()

# the only difference with persistence window is, we create windows here at startup of application
# and then we show then when required,
# rather than creating and showing (both) when required. (as in previous cases)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
