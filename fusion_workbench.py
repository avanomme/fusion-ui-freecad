import FreeCADGui
from PySide2 import QtWidgets, QtCore
from layout.main_panel import MainPanel

class FusionWorkbench(FreeCADGui.Workbench):
    MenuText = "Fusion"
    ToolTip = "Fusion-style UI workbench with tabbed toolbar"
    Icon = "icons/FusionWorkbench.svg"  # Optional: put your icon here

    def __init__(self):
        self.panel = None

    def Initialize(self):
        self.panel = MainPanel()
        self.dock = QtWidgets.QDockWidget("Fusion UI", FreeCADGui.getMainWindow())
        self.dock.setObjectName("FusionDock")
        self.dock.setWidget(self.panel)
        FreeCADGui.getMainWindow().addDockWidget(QtCore.Qt.TopDockWidgetArea, self.dock)

    def Activated(self):
        if self.dock:
            self.dock.show()

    def Deactivated(self):
        if self.dock:
            self.dock.hide()

    def ContextMenu(self, recipient):
        pass

    def GetClassName(self):
        return "Gui::PythonWorkbench"