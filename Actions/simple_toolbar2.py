import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QAction, QStatusBar
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My Awesome App")

        label = QLabel("Hello")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        # set the size of icons on toolbar
        toolbar.setIconSize(QSize(16, 16))
        # toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(toolbar)

        # first param: the icon
        button_action = QAction(QIcon("bug.png"), "Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

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