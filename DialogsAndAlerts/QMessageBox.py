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
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Question")
        dlg.setText("Are you sure?")
        # all the buttons present in QDialogBox are present in QMessageBox
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()

        if button == QMessageBox.Ok:
            print("Ok")

# Icon state	                Description
# QMessageBox.NoIcon	        The message box does not have an icon.
# QMessageBox.Question	        The message is asking a question.
# QMessageBox.Information	    The message is informational only.
# QMessageBox.Warning	        The message is warning.
# QMessageBox.Critical	        The message indicates a critical problem.


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()