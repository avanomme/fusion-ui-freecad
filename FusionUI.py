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
        """Create the 3-level Fusion 360-style ribbon interface"""
        # 1. Top-level workspace tabs (only Solid active for now)
        self.workspace_tabs = QtGui.QTabBar()
        self.workspace_tabs.addTab("SOLID")
        self.workspace_tabs.addTab("SURFACE")
        self.workspace_tabs.addTab("MESH")
        self.workspace_tabs.addTab("SHEET METAL")
        self.workspace_tabs.addTab("PLASTIC")
        self.workspace_tabs.addTab("UTILITIES")
        self.workspace_tabs.addTab("MANAGE")
        self.workspace_tabs.setCurrentIndex(0)
        self.app.addToolBarBreak()
        self.app.addToolBar(QtCore.Qt.TopToolBarArea, self._wrap_widget(self.workspace_tabs))

        # 2. Quick access toolbar sections (Create, Modify, etc.)
        self.section_toolbar = QtGui.QToolBar("Fusion Quick Access")
        self.section_toolbar.setMovable(False)
        self.app.addToolBar(self.section_toolbar)

        # Add quick access buttons for each section
        self.create_section_button = QtGui.QToolButton()
        self.create_section_button.setText("CREATE")
        self.create_section_button.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.create_section_button.setMenu(self.create_create_menu())
        self.section_toolbar.addWidget(self.create_section_button)
        # (Add more section buttons here: Modify, Assemble, etc.)

    def _wrap_widget(self, widget):
        """Wrap a QWidget in a QToolBar for placement in the main window."""
        toolbar = QtGui.QToolBar()
        toolbar.addWidget(widget)
        toolbar.setMovable(False)
        return toolbar

    def create_create_menu(self):
        """Create the dropdown menu for the Create section in Solid workspace."""
        menu = QtGui.QMenu()
        create_actions = [
            ("Create Sketch", "Sketcher_NewSketch"),
            ("Extrude (Pad)", "PartDesign_Pad"),
            ("Extrude (Part)", "Part_Extrude"),
            ("Revolve (Part Design)", "PartDesign_Revolution"),
            ("Revolve (Part)", "Part_Revolve"),
            ("Sweep (Part)", "Part_Sweep"),
            ("Sweep (Additive)", "PartDesign_AdditivePipe"),
            ("Loft (Part)", "Part_Loft"),
            ("Loft (Additive)", "PartDesign_AdditiveLoft"),
            ("Box", "Part_Box"),
            ("Cylinder", "Part_Cylinder"),
            ("Sphere", "Part_Sphere"),
            ("Torus", "Part_Torus"),
            ("Coil (Helix)", "Part_Helix"),
            ("Pipe (Sweep)", "Part_Sweep"),
            ("Mirror", "PartDesign_Mirrored"),
            ("Pattern (Linear)", "PartDesign_LinearPattern"),
            ("Pattern (Circular)", "PartDesign_PolarPattern"),
            ("Shell (Thickness)", "PartDesign_Thickness"),
            ("Fillet", "PartDesign_Fillet"),
            ("Chamfer", "PartDesign_Chamfer"),
            ("Combine (Union)", "Part_Union"),
            ("Combine (Cut)", "Part_Cut"),
            ("Combine (Intersect)", "Part_Common"),
            ("Create Body", "PartDesign_Body"),
            ("Move/Copy", "Std_Placement"),
            ("Project Geometry", "Sketcher_External")
        ]
        for label, cmd in create_actions:
            icon_path = self.get_icon_path(label)
            if icon_path:
                icon = QtGui.QIcon(icon_path)
                action = menu.addAction(icon, label)
            else:
                action = menu.addAction(label)
            action.triggered.connect(lambda checked, c=cmd: FreeCADGui.runCommand(c,0))
        return menu

    def get_icon_path(self, tool):
        """Return the icon path for a given tool name, matching Fusion 360 icons where possible."""
        icon_map = {
            "Create Sketch": "solid_-_web_-_32x32.png",
            "Extrude (Pad)": "solid_-_web_-_32x32.png",
            "Extrude (Part)": "solid_-_web_-_32x32.png",
            "Revolve (Part Design)": "solid_-_web_-_32x32.png",
            "Revolve (Part)": "solid_-_web_-_32x32.png",
            "Sweep (Part)": "solid_-_web_-_32x32.png",
            "Sweep (Additive)": "solid_-_web_-_32x32.png",
            "Loft (Part)": "solid_-_web_-_32x32.png",
            "Loft (Additive)": "solid_-_web_-_32x32.png",
            "Box": "solid_-_web_-_32x32.png",
            "Cylinder": "solid_-_web_-_32x32.png",
            "Sphere": "solid_-_web_-_32x32.png",
            "Torus": "solid_-_web_-_32x32.png",
            "Coil (Helix)": "solid_-_web_-_32x32.png",
            "Pipe (Sweep)": "solid_-_web_-_32x32.png",
            "Mirror": "solid_-_web_-_32x32.png",
            "Pattern (Linear)": "solid_-_web_-_32x32.png",
            "Pattern (Circular)": "solid_-_web_-_32x32.png",
            "Shell (Thickness)": "solid_-_web_-_32x32.png",
            "Fillet": "solid_-_web_-_32x32.png",
            "Chamfer": "solid_-_web_-_32x32.png",
            "Combine (Union)": "solid_-_web_-_32x32.png",
            "Combine (Cut)": "solid_-_web_-_32x32.png",
            "Combine (Intersect)": "solid_-_web_-_32x32.png",
            "Create Body": "solid_-_web_-_32x32.png",
            "Move/Copy": "solid_-_web_-_32x32.png",
            "Project Geometry": "solid_-_web_-_32x32.png"
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