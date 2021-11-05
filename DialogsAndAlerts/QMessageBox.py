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
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a simple dialog")
        button = dlg.exec()

        if button == QMessageBox.Ok:
            print("Ok")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()