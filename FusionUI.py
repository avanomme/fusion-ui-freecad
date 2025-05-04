import FreeCAD
import FreeCADGui
from PySide import QtCore, QtGui
import os

class FusionUI:
    def __init__(self):
        self.app = FreeCADGui.getMainWindow()
        self.ribbon_style = """
        QToolBar {
            background-color: #2d2d2d;
            border: none;
            spacing: 2px;
        }
        QToolButton {
            background-color: transparent;
            border: none;
            padding: 4px;
            margin: 2px;
        }
        QToolButton:hover {
            background-color: #3d3d3d;
        }
        """
        
    def setup(self):
        """Setup the Fusion 360 style interface"""
        self.setup_ribbon()
        self.setup_shortcuts()
        self.apply_style()
        
    def setup_ribbon(self):
        """Create the ribbon-style interface"""
        # Create main ribbon toolbar
        self.ribbon = self.app.addToolBar("Fusion Ribbon")
        self.ribbon.setMovable(False)
        
        # Add tabs (Create, Modify, etc.)
        self.create_tabs()
        
    def create_tabs(self):
        """Create the main tabs similar to Fusion 360"""
        tabs = {
            "Create": ["Sketch", "Extrude", "Revolve", "Sweep"],
            "Modify": ["Fillet", "Chamfer", "Shell", "Pattern"],
            "Assemble": ["New Component", "Joint", "Align"],
            "Inspect": ["Measure", "Section Analysis"]
        }
        
        for tab_name, tools in tabs.items():
            self.add_tab(tab_name, tools)
            
    def add_tab(self, name, tools):
        """Add a tab with its tools to the ribbon"""
        tab = QtGui.QToolBar(name)
        for tool in tools:
            icon_path = self.get_icon_path(tool)
            if icon_path:
                icon = QtGui.QIcon(icon_path)
                action = QtGui.QAction(icon, tool, self.app)
            else:
                action = QtGui.QAction(tool, self.app)
            tab.addAction(action)
        self.ribbon.addWidget(tab)
        
    def get_icon_path(self, tool):
        """Return the icon path for a given tool name, matching Fusion 360 icons where possible."""
        icon_map = {
            "Create Sketch": "solid_-_api_-_32x32.png",
            "Extrude": "solid_-_api_-_32x32.png",
            "Revolve": "solid_-_api_-_32x32.png",
            "Sweep": "solid_-_api_-_32x32.png",
            "Loft": "solid_-_api_-_32x32.png",
            "Rib": "solid_-_api_-_32x32.png",
            "Web": "solid_-_api_-_32x32.png",
            "Emboss": "solid_-_api_-_32x32.png",
            "Hole": "solid_-_api_-_32x32.png",
            "Thread": "solid_-_api_-_32x32.png",
            "Box": "solid_-_api_-_32x32.png",
            "Cylinder": "solid_-_api_-_32x32.png",
            "Sphere": "solid_-_api_-_32x32.png",
            "Torus": "solid_-_api_-_32x32.png",
            "Coil": "solid_-_api_-_32x32.png",
            "Pipe": "solid_-_api_-_32x32.png",
            "Pattern": "solid_-_api_-_32x32.png",
            "Mirror": "solid_-_api_-_32x32.png",
            "Thicken": "solid_-_api_-_32x32.png",
            "Boundary Fill": "solid_-_api_-_32x32.png",
            "Create Base Feature": "solid_-_api_-_32x32.png",
            "Create PCB": "solid_-_api_-_32x32.png"
        }
        filename = icon_map.get(tool)
        if filename:
            return os.path.join(os.path.dirname(__file__), "icons", filename)
        return None
        
    def setup_shortcuts(self):
        """Setup Fusion 360 style shortcuts"""
        shortcuts = {
            "Sketch": "S",
            "Extrude": "E",
            "Revolve": "R",
            "Fillet": "F",
            "Chamfer": "C",
            "Measure": "M"
        }
        
        for action, shortcut in shortcuts.items():
            self.set_shortcut(action, shortcut)
            
    def set_shortcut(self, action_name, shortcut):
        """Set a shortcut for an action"""
        for action in self.app.findChildren(QtGui.QAction):
            if action.text() == action_name:
                action.setShortcut(shortcut)
                
    def apply_style(self):
        """Apply the Fusion 360 style to the interface"""
        self.app.setStyleSheet(self.ribbon_style)
        
    def create_sketch(self):
        """Create a new sketch"""
        FreeCADGui.runCommand('Sketcher_NewSketch', 0)
        
    def extrude(self):
        """Create an extrusion"""
        FreeCADGui.runCommand('Part_Extrude', 0)
        
    def revolve(self):
        """Create a revolution"""
        FreeCADGui.runCommand('Part_Revolve', 0) 