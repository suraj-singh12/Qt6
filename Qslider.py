import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        self.setMinimumSize(QSize(400, 300))

        # QSlider provides a slide-bar widget, which functions internally much like a QDoubleSpinBox.
        # Rather than display the current value numerically, it is represented by the position of
        # the slider handle along the length of the widget.
        # This is often useful when providing adjustment between two extremes,
        # but where absolute accuracy is not required.
        # The most common use of this type of widget is for volume controls.
        widget = QSlider(Qt.Horizontal)     # Qt.Horizontal is the orientation of slider
        # another valid orientation is Qt.Vertical

        widget.setMinimum(-10)
        widget.setMaximum(3)
        # or : widget.setRange(-10,3)

        widget.setSingleStep(3)

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
        print("Pressed")

    def slider_released(self):
        print("Released")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()