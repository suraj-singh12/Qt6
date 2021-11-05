import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QAction, QStatusBar, QCheckBox, QLineEdit, QVBoxLayout, QWidget
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My Awesome App")
        self.setMinimumSize(QSize(400, 300))

        # set a simple label on current window
        # ---------------------------------------------------
        label = QLabel("Hello")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)
        # ---------------------------------------------------

        # toolbar
        # ---------------------------------------------------
        # create toolbar
        toolbar = QToolBar("My main toolbar")
        # set the size of icons on toolbar
        toolbar.setIconSize(QSize(16, 16))
        # toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        # add the toolbar to current window (base presently)
        self.addToolBar(toolbar)

        # NOTE: for QAction the parent element is passed in as the final parameter (always)
        # button1
        button_action = QAction(QIcon("bug.png"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        # separator
        toolbar.addSeparator()

        # button2
        button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
        button_action2.setStatusTip("This is also your button")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addSeparator()

        # button3
        button_action3 = QAction(QIcon("bug.png"), "alarm", self)
        button_action3.setStatusTip("This is alarm")
        button_action3.triggered.connect(self.onMyToolBarButtonClick)
        button_action3.setCheckable(True)
        toolbar.addAction(button_action3)

        toolbar.addSeparator()

        # a simple label
        label = QLabel("Hii")
        # label added to toolbar
        toolbar.addWidget(label)

        toolbar.addSeparator()

        # checkbox added to toolbar
        toolbar.addWidget(QCheckBox("checkMe"))

        toolbar.addSeparator()

        # single line i/p box added to toolbar
        one_line = QLineEdit()
        one_line.setPlaceholderText("Enter your line")
        toolbar.addWidget(one_line)

        # adding multiple widgets at one place using QVBoxLayout(will make toolbar bit ugly, but it's practise)
        # try commenting then uncommenting below code
        # -------------------------------------
        # layout
        vertical_layout = QVBoxLayout()
        # single line i/p box in layout : box1
        line1 = QLineEdit()
        line1.setPlaceholderText("line1")
        vertical_layout.addWidget(line1)
        # single line i/p box in layout : box2
        line2 = QLineEdit()
        line2.setPlaceholderText("Line2")
        vertical_layout.addWidget(line2)

        # simple widget
        widget = QWidget()
        # layout applied on this widget
        widget.setLayout(vertical_layout)
        # this simple widget added to toolbar
        toolbar.addWidget(widget)
        # -------------------------------------

        toolbar.addSeparator()

        # default status bar
        self.setStatusBar(QStatusBar(self))

        # ---------------------------------------------------

    def onMyToolBarButtonClick(self, s):
        print("click", s)

# Note that Qt uses your operating system default settings to determine
# whether to show an icon, text or an icon and text in the toolbar.
# But you can override this by using .setToolButtonStyle.
# This slot accepts any of the following flags from the Qt. namespace:
#
# PyQt5 flag	                        Behavior
# Qt.ToolButtonIconOnly	                Icon only, no text
# Qt.ToolButtonTextOnly	                Text only, no icon
# Qt.ToolButtonTextBesideIcon	        Icon and text, with text beside the icon
# Qt.ToolButtonTextUnderIcon	        Icon and text, with text under the icon
# Qt.ToolButtonFollowStyle	            Follow the host desktop style
#
# toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
# Qt.ToolButtonFollowStyle: (default) generally recommended to make your application feel as native as possible.


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()