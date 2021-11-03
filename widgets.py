import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        Widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in Widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

'''
Widget	        What it does
QCheckbox	     A checkbox
QComboBox	    A dropdown list box
QDateEdit	    For editing dates and datetimes
QDateTimeEdit	For editing dates and datetimes
QDial	        Rotatable dial
QDoubleSpinbox	A number spinner for floats
QFontComboBox	A list of fonts
QLCDNumber	    A quite ugly LCD display
QLabel	        Just a label, not interactive
QLineEdit	    Enter a line of text
QProgressBar	A progress bar
QPushButton	    A button
QRadioButton	A toggle set, with only one active item
QSlider	        A slider
QSpinBox	    An integer spinner
QTimeEdit	    For editing times
'''



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()