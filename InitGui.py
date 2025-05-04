# InitGui.py
import FreeCADGui
from fusion_workbench import FusionWorkbench

class FusionWorkbenchLoader:
    def __init__(self):
        pass

    def Initialize(self):
        FreeCADGui.addWorkbench(FusionWorkbench())

    def GetClassName(self):
        return "Gui::PythonWorkbench"

Gui = FusionWorkbenchLoader()