import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize

# > QApplication: the application handler and
# > QWidget: a basic empty GUI widget
# both from the QtWidgets module.

# > QMainWindow: This is a pre-made widget which provides a lot of standard window features
# you'll make use of in your apps, including toolbars, menus, a statusbar, dockable widgets and more.

# In Qt sizes are defined using a "QSize" object. This accepts width and height parameters in that order.


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")
        button = QPushButton("Press Me!")

        self.setMinimumSize(QSize(400,150))
        self.setMaximumSize(QSize(600,400))

        # setting the window as fixed size, this will disable resizing capability
        # self.setFixedSize(QSize(400,400))
        self.setCentralWidget(button)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Window = QWidget()  # Window = QPushButton("push me")

# Create a Qt widget, which will be our window.
Window = MainWindow()
Window.show()       # IMPORTANT!!!!! Windows are hidden by default.

# start the event loop
app.exec()
