import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

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
    # we create the CustomDialog instance
    # This will make the dialog a modal window of QMainWindow.
    # This means the dialog will completely block interaction with the parent window.

    def button_clicked(self, s):
        print("click", s)
        dlg = CustomDialog(self)
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

# Note: QDialog completely blocks your application execution. Don't start a
# dialog and expect anything else to happen anywhere else in your app.
# However, after knowing threads & processes, there is a way to get out of this pickle.


class CustomDialog(QDialog):        # CustomDialog (subclass of QDialog)
    def __init__(self, parent=None):
        super(CustomDialog, self).__init__()

        # applying customizations
        self.setWindowTitle("HELLO!")

        # this will show an OK and a Cancel button
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        # QBtn now contains an integer value representing the two buttons.

        # instead of using QButton we are using namespace attributes from QDialogButtonBox
        # because it ensures that your dialog respects the host desktop standards
        # (OK on left vs. right for example)

        # creating QDialogButtonBox() instance to hold the buttons
        self.buttonBox = QDialogButtonBox(QBtn)
        # connecting QDialogButtonBox signals to correct slots on dialog
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        # To make the buttons have any effect, you must connect the correct
        # QDialogButtonBox signals to the slots on the dialog.
        # In our case we've connected the .accepted and .rejected signals
        # from the QDialogButtonBox to the handlers for .accept() and
        # .reject() on our subclass of QDialog.

        # to make the QDialogButtonBox appear in our dialog box we must
        # add it to the dialog layout.

        # So, as for the main window we create a layout,
        # and add our QDialogButtonBox to it (QDialogButtonBox is a widget),
        # and then set that layout on our dialog.

        # creating the layout
        self.layout = QVBoxLayout()

        message = QLabel("Something happened, is that OK?")
        # adding widgets to layout
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        # set the layout on dialog
        self.setLayout(self.layout)

        # Finally, we launch this CustomDialog in our MainWindow.button_clicked slot.


# The full list of available buttons :
#
# QDialogButtonBox.Ok
# QDialogButtonBox.Open
# QDialogButtonBox.Save
# QDialogButtonBox.Cancel
# QDialogButtonBox.Close
# QDialogButtonBox.Discard
# QDialogButtonBox.Apply
# QDialogButtonBox.Reset
# QDialogButtonBox.RestoreDefaults
# QDialogButtonBox.Help
# QDialogButtonBox.SaveAll
# QDialogButtonBox.Yes
# QDialogButtonBox.YesToAll
# QDialogButtonBox.No
# QDialogButtonBox.Abort
# QDialogButtonBox.Retry
# QDialogButtonBox.Ignore
# QDialogButtonBox.NoButton


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()