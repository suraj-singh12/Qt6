import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setMinimumSize(QSize(400, 300))
        self.setWindowTitle("My App")

        # QDial is a rotatable widget that functions just like the slider,
        # but appears as an analogue dial.
        widget = QDial()

        widget.setRange(-40, 80)
        widget.setSingleStep(5)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("Position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()