import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    # def button_clicked(self, s):
    #     button = QMessageBox.about(self, "About", "Created By: Suraj Singh")

    def button_clicked(self, s):
        # all this can be applied to warning, information, question also
        button = QMessageBox.critical(
            self,
            "Oh man!",
            "Something Went Wrong.",
            buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard,
        )

        if button == QMessageBox.Discard:
            print("Discard!")
        elif button == QMessageBox.NoToAll:
            print("No to all!")
        else:
            print("Ignore!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()