import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize


# > QApplication: the application handler (holds the Qt event loop, only one instance required)
# > QWidget: a basic empty GUI widget
# both from the QtWidgets module.

# > QMainWindow: This is a pre-made widget which provides a lot of standard window features
# you'll make use of in your apps, including toolbars, menus, a statusbar, dockable widgets and more.

# In Qt sizes are defined using a "QSize" object. This accepts width and height parameters in that order.

# -------------------------------------------------------------------------------------------------------
# Signals: Signals are notifications emitted by widgets when something happens.
# That something can be any number of things, from pressing a button,
# to the text of an input box changing, to the text of the window changing.
# Many signals are initiated by user action, but this is not a rule.
# In addition to notifying about something happening,
# signals can also send data to provide additional context about what happened.

# Slots: Slots is the name Qt uses for the receivers of signals.
# In Python any function (or method) in your application can be used as a slot
# -- simply by connecting the signal to it. If the signal sends data,
# then the receiving function will receive that data too.
# Many Qt widgets also have their own built-in slots, meaning you can hook Qt widgets together directly.


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")
        self.button = QPushButton("Press Me!")
        self.button_is_checked = True

        self.button.setCheckable(True)
        self.button.released.connect(self.button_was_released)
        # self.button.setChecked(self.button_is_checked)
        # button.clicked.connect(self.button_was_toggled)

        self.setMinimumSize(QSize(400, 150))
        self.setMaximumSize(QSize(600, 400))
        # setting the window as fixed size, this will disable resizing capability
        # self.setFixedSize(QSize(400,400))
        self.setCentralWidget(self.button)

    def button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)

    def button_was_clicked(self):
        print("clicked !")

    def button_was_toggled(self, checked):
        # print("Checked?",checked)
        self.button_is_checked = checked
        print(self.button_is_checked)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Window = QWidget()  # Window = QPushButton("push me")

# Create a Qt widget, which will be our window.
Window = MainWindow()
Window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# start the event loop
app.exec()
