import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        # self.setMinimumSize(400, 300)

        # The QComboBox is a drop down list, closed by default
        # with an arrow to open it.You can select a single item from the list,
        # with the currently selected item being shown as a label on the widget.
        # The combo box is suited to selection of a choice from a long list of options.
        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])

        # sends the current index of the selected item
        widget.currentIndexChanged.connect(self.index_changed)

        # There is an alternate signal to send the text
        widget.currentTextChanged.connect(self.text_changed)

        # QComboBox can also be editable, allowing users to enter values not currently
        # in the list and either have them inserted, or simply used as a value.
        # To make the box editable:
        widget.setEditable(True)
        widget.setInsertPolicy(QComboBox.InsertAlphabetically)
        widget.setMaxCount(4)

        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i)

    def text_changed(self, s):
        print(s)


'''
You can also set a flag to determine how the insert is handled. These flags are stored on the QComboBox class itself and are listed below:

PyQt5 flag	                    Behavior
QComboBox.NoInsert	            No insert
QComboBox.InsertAtTop	        Insert as first item
QComboBox.InsertAtCurrent	    Replace currently selected item
QComboBox.InsertAtBottom	    Insert after last item
QComboBox.InsertAfterCurrent	Insert after current item
QComboBox.InsertBeforeCurrent	Insert before current item
QComboBox.InsertAlphabetically	Insert in alphabetical order

To use these, apply the flag as follows:
widget.setInsertPolicy(QComboBox.InsertAlphabetically)

You can also limit the number of items allowed in the box by using .setMaxCount, e.g.
widget.setMaxCount(10)
'''

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()