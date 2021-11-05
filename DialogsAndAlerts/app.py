import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# "Dialogs"
# Dialogs are useful GUI components that allow you to communicate with the user
# (hence the name dialog). They are commonly used for file Open/Save, settings,
# preferences, or for functions that do not fit into the main UI of the
# application. They are small modal (or blocking) windows that sit in front of
# the main application until they are dismissed. Qt provides a number of
# 'special' built-in dialogs for the most common use-cases,
# allowing you to provide a platform-native user experience.

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
