import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QAction, QStatusBar, QCheckBox, QLineEdit, QVBoxLayout, QWidget
)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt, QSize

# QAction is a class that provides a way to describe abstract user interfaces.
# What this means in English, is that you can define multiple interface elements within
# a single object, unified by the effect that interacting with that element has.
# For example, it is common to have functions that are represented in the toolbar
# but also the menu — think of something like Edit->Cut which is present both in the
# Edit menu but also on the toolbar as a pair of scissors, and also through the
# keyboard shortcut Ctrl-X (Cmd-X on Mac). Without QAction you would have to define this in multiple places.

# Each QAction has names, status messages, icons and signals that you can connect to (and much more).


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My Awesome App")
        # self.setMinimumSize(QSize(400, 300))

        # set a simple label on current window
        # ---------------------------------------------------
        label = QLabel("Hello")
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)
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
        # keyboard shortcuts can be entered in 3 ways:
        # 1. directly using key names (example): Ctrl+p
        # 2. using Qt.namespace identifiers (eg. Qt.CTRL + Qt.Kwy_P)
        # 3. using system agnostic identifiers (eg. QKeySequence.Print)
        button_action.setShortcut(QKeySequence("Ctrl+1"))
        toolbar.addAction(button_action)

        # separator
        toolbar.addSeparator()

        # button2
        button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
        button_action2.setStatusTip("This is also your button")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        button_action2.setShortcut(QKeySequence("Ctrl+2"))
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

        # =====================================================================
        menu = self.menuBar()
        # adding a menu
        file_menu = menu.addMenu("&File")
        # adding actions to 'File' menu
        file_menu.addAction(button_action)
        file_menu.addSeparator()

        file_submenu = file_menu.addMenu("submenu")
        file_submenu.addAction(button_action2)
        # =======================================================================

    def onMyToolBarButtonClick(self, s):
        print("click", s)

# Note that the keyboard shortcut is associated with the QAction and will
# still work whether or not the QAction is added to a menu or a toolbar.

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
