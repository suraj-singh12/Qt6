import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setMinimumSize(QSize(400,300))
        self.setWindowTitle("My App")

        widget = QSpinBox()
        # or: widget = QDoubleSpinBox

        widget.setMinimum(-20)
        widget.setMaximum(5)
        # or: widget.setRange(-20,5)

        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(3)     # or: example 0.5 for doubleSpinBox
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def value_changed_str(self, s):
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()