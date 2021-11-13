"""
Loading the dialog's gui with uic.loadUi()
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # create a Button
        self.centralWidget = QPushButton("Employee...")
        # connect the clicked signal with onEmployeeBtnClicked slot (this will launch the employee dialog)
        self.centralWidget.clicked.connect(self.onEmployeeBtnClicked)
        # set the button as central widget of main-window
        self.setCentralWidget(self.centralWidget)

    def onEmployeeBtnClicked(self):
        """  launch the employee dialog """
        dlg = Employee()
        dlg.exec()


class Employee(QDialog):
    def __init__(self, parent=None):
        super(Employee, self).__init__(parent)
        " load the dialog's gui "
        loadUi("employee.ui", self)


if __name__ == "__main__":
    # create the application
    app = QApplication(sys.argv)
    # create and show the application's main window
    window = MainWindow()
    window.show()
    # run the application's main loop
    sys.exit(app.exec())