import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# QMessageBox: used to create information, warning, about, or question dialogs
# This we can do by custom QDialogBox, but Qt provides these built-in dialog to us


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        button = QMessageBox.question(self, "Question Dialog", "Are you sure?")

        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No!")

# Icon state	                Description
# QMessageBox.NoIcon	        The message box does not have an icon.
# QMessageBox.Question	        The message is asking a question.
# QMessageBox.Information	    The message is informational only.
# QMessageBox.Warning	        The message is warning.
# QMessageBox.Critical	        The message indicates a critical problem.

# To make things more simpler, QMessageBox dialogs have a number of methods
# which can be used to construct these types of message dialog

# QMessageBox.about(parent, title, message)
# QMessageBox.critical(parent, title, message)
# QMessageBox.information(parent, title, message)
# QMessageBox.question(parent, title, message)
# QMessageBox.warning(parent, title, message)

# The parent parameter is the window which the dialog will be a child of.
# If you're launching your dialog from your main window, you can just pass in self


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()