class FusionWorkbenchLoader:
    """Initializes the Fusion UI workbench when FreeCAD starts."""
    def Initialize(self):
        import fusion_workbench # Import the module containing the workbench class

    def GetClassName(self):
        # This must be the name of the workbench class
        return "FusionWorkbench"

# Register the workbench loader
FreeCADGui.addCommand('FusionUI_Workbench', FusionWorkbenchLoader()) 