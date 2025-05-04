from PySide2 import QtWidgets

class SolidToolbar(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Solid Tools Placeholder")
        layout.addWidget(label)
        self.setLayout(layout)