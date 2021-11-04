import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPalette, QColor

'''
four basic type of layout exist in PyQt5

Layout	            Behaviour
QHBoxLayout	        Linear horizontal layout
QVBoxLayout	        Linear vertical layout
QGridLayout	        In indexable grid XxY
QStackedLayout	    Stacked (z) in front of one another

You can also design and lay out your interface graphically using the Qt designer.
Here we're using code, so you can understand the underlying system.
'''


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

app = QApplication(sys.argv)
window = MainWindow()
window.close()

app.exec()