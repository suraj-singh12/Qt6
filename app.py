import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")
        button = QPushButton("Press Me!")

        self.setCentralWidget(button)


# passing command line args to application
app = QApplication(sys.argv)

# Window = QWidget()  #QPushButton("push me")
Window = MainWindow()
Window.show()

app.exec()
