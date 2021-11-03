import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setMinimumSize(QSize(350, 200))

        # QLabel : simple one-line piece of text you can position in your application
        widget = QLabel("Hello")
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)

        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(widget)

        # update the text of label
        # widget.setText("Updated Hello")

        # label can also be used to display images
        self.setWindowTitle("Windows 11 Upgrade")
        widget.setPixmap(QPixmap('image1.png'))
        # By default the image scales while maintaining its aspect ratio.
        # If you want to stretch an scale to fit the window completely you can set
        # .setScaledContents(True)

        # first we need to make window size fixed, in order to see the effect of .setScaledContents(True)
        self.setFixedSize(QSize(1620, 300))

        widget.setScaledContents(True)


'''
The flags available for horizontal alignment are:

PyQt5 flag	        Behavior
Qt.AlignLeft	    Aligns with the left edge.
Qt.AlignRight	    Aligns with the right edge.
Qt.AlignHCenter	    Centers horizontally in the available space.
Qt.AlignJustify	    Justifies the text in the available space.

The flags available for vertical alignment are:

PyQt5 flag	        Behavior
Qt.AlignTop	        Aligns with the top.
Qt.AlignBottom	    Aligns with the bottom.
Qt.AlignVCenter	    Centers vertically in the available space.

You can combine flags together using pipes (|), 
however note that you can only use vertical or horizontal alignment flag at a time.

Finally, there is also a shorthand flag that centers in both directions simultaneously:

PyQt5 Flag	        Behavior
Qt.AlignCenter	    Centers horizontally and vertically
'''


app = QApplication(sys.argv)
w = MainWindow()
w.show()

app.exec()