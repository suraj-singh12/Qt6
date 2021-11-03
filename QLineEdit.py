import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("My App")

        # The QLineEdit widget is a simple single - line text editing box,
        # into which users can type input.These are used
        # for form fields, or settings where there is no restricted list of valid inputs.
        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text")

        # widget.setReadOnly(True)  # to make the box readOnly
        # widget.setInputMask('000.000.00')

        widget.returnPressed.connect(self.return_pressed)       # triggered when enter is pressed
        widget.selectionChanged.connect(self.selection_changed) # triggered when any text is selected
        widget.textChanged.connect(self.text_changed)   # triggered when text changed
        widget.textEdited.connect(self.text_edited)     # triggered when text edited
        # There are also two edit signals, one for when the text in the box has been edited and
        # one for when it has been changed.
        # The distinction here is between user edits and programmatic changes.
        # The textEdited signal is only sent when the user edits text.

        # Additionally, it is possible to perform input validation using an input mask
        # to define which characters are supported and where.
        # This can be applied to the field as follows :

        # widget.setInputMask('000.000.000.000;_')
        # The above would allow a series of 3-digit numbers separated with periods,
        # and could therefore be used to validate IPv4 addresses.

        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
