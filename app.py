import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget

from PyQt5.QtCore import QSize, Qt

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
# --------------------------------------------------------------------------------------------------------
# Events: Every interaction the user has with a Qt application is an event.
# --------------------------------------------------------------------------------------------------------


import sys
from random import choice


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Click Events")
        self.setFixedSize(QSize(350, 240))

        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mousePressEvent LEFT")
        elif e.button() == Qt.RightButton:
            self.label.setText("mousePressEvent RIGHT")
        elif e.button() == Qt.MiddleButton:
            self.label.setText("mousePressEvent MIDLLE")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")
        elif e.button() == Qt.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")
        elif e.button() == Qt.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDLLE")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")
        elif e.button() == Qt.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")
        elif e.button() == Qt.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDLLE")


'''
Method	Returns
.button()	Specific button that triggered this event
.buttons()	State of all mouse buttons (OR'ed flags)
.globalPos()	Application-global position as a QPoint
.globalX()	Application-global horizontal X position
.globalY()	Application-global vertical Y position
.pos()	Widget-relative position as a QPoint integer
.posF()	Widget-relative position as a QPointF float
'''

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
