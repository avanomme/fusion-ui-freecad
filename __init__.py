import FreeCAD
import FreeCADGui
import os
import sys

class FusionUIWorkbench(FreeCADGui.Workbench):
    """Fusion 360 style UI workbench for FreeCAD"""

    MenuText = "Fusion UI"
    ToolTip = "Fusion 360 style interface"
    Icon = os.path.join(os.path.dirname(__file__), "icons", "fusion_icon.svg")

    def Initialize(self):
        """Initialize the workbench"""
        from .FusionUI import FusionUI
        self.ui = FusionUI()
        self.ui.setup()

    def Activated(self):
        """Activate the workbench"""
        pass

    def Deactivated(self):
        """Deactivate the workbench"""
        pass

    def ContextMenu(self, recipient):
        """Context menu for the workbench"""
        pass

    def GetClassName(self):
        """Return the class name"""
        return "Gui::PythonWorkbench"

# Add the workbench to FreeCAD
FreeCADGui.addWorkbench(FusionUIWorkbench()) 