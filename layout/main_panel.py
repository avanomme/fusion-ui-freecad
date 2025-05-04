from PySide2 import QtWidgets
from layout.toolbar_solid import SolidToolbar
from layout.toolbar_mesh import MeshToolbar

class MainPanel(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        # Fusion-style top tab bar
        self.tab_bar = QtWidgets.QTabBar()
        self.tab_bar.addTab("Solid")
        self.tab_bar.addTab("Mesh")
        self.tab_bar.setShape(QtWidgets.QTabBar.RoundedNorth)
        self.tab_bar.setStyleSheet("""
            QTabBar::tab {
                background: #2C2C2C;
                color: white;
                padding: 8px 16px;
                margin-right: 4px;
                font-weight: bold;
            }
            QTabBar::tab:selected {
                background: #3E8EDE;
                color: white;
            }
        """)
        self.layout.addWidget(self.tab_bar)

        # Stack to switch between toolbars
        self.stack = QtWidgets.QStackedWidget()
        self.solid_toolbar = SolidToolbar()
        self.mesh_toolbar = MeshToolbar()
        self.stack.addWidget(self.solid_toolbar)
        self.stack.addWidget(self.mesh_toolbar)
        self.layout.addWidget(self.stack)

        # Wire tab switching
        self.tab_bar.currentChanged.connect(self.stack.setCurrentIndex)
        self.stack.setCurrentIndex(0)