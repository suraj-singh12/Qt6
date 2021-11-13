import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton
# pyuic5 employee.ui -o employee.py
# above command creates a python file from the UI file
from employee import Ui_Dialog


class Window(QMainWindow):
    """  Main Window """
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # create a button
        self.centralWidget = QPushButton("Employee...")
        # connect the clicked signal to onEmployeeBtnClicked slot
        self.centralWidget.clicked.connect(self.onEmployeeBtnClicked)
        # set the button as central widget of main-window
        self.setCentralWidget(self.centralWidget)

    # create a slot for launching employee dialog
    def onEmployeeBtnClicked(self):
        dlg = Employee(self)
        dlg.exec()


class Employee(QDialog):
    """  Employee dialog """
    def __init__(self, parent=None):
        super(Employee, self).__init__(parent)

        # create an instance of GUI
        self.ui = Ui_Dialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)


if __name__ == "__main__":
    # create the application
    app = QApplication(sys.argv)
    # create and show the application's main window
    window = Window()
    window.show()
    # run the application's main loop
    sys.exit(app.exec())

