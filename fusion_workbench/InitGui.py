import FreeCADGui
from .fusion_workbench import FusionWorkbench

# Register the workbench with FreeCAD
FreeCADGui.addWorkbench(FusionWorkbench())
