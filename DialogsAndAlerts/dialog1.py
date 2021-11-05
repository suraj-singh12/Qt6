import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton
from PyQt5.QtCore import QSize

# In Qt dialog boxes are handled by the QDialog class.
# To create a new dialog box simply create a new object of
# QDialog type passing in another widget, e.g. QMainWindow, as its parent.


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        self.setMinimumSize(QSize(300, 100))

        button = QPushButton("Press me for a dialog")
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

    # In the slot button_clicked (which receives the signal from the button press)
    # we create the dialog instance, passing our QMainWindow instance as a parent.
    # This will make the dialog a modal window of QMainWindow.
    # This means the dialog will completely block interaction with the parent window.

    def button_clicked(self, s):
        print("click", s)

        dlg = QDialog(self)
        dlg.setWindowTitle("HELLO")
        dlg.setMinimumSize(QSize(200, 80))
        dlg.exec()

# Note: QDialog completely blocks your application execution. Don't start a
# dialog and expect anything else to happen anywhere else in your app.
# However, after knowing threads & processes, there is a way to get out of this pickle.


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()