import FreeCAD
import FreeCADGui
from FreeCAD import Base
import re


def generate_from_text(text):
    """Generate basic FreeCAD primitives from simple text commands.

    Supported commands:
    - "cube <length>" -> creates a cube with side length
    - "box <l> <w> <h>" -> creates a box with dimensions
    - "cylinder <radius> <height>" -> creates a cylinder
    """
    text = text.lower().strip()
    doc = FreeCAD.ActiveDocument
    if doc is None:
        doc = FreeCAD.newDocument()

    cube_match = re.match(r"cube\s+(\d+(?:\.\d+)?)", text)
    if cube_match:
        size = float(cube_match.group(1))
        obj = doc.addObject("Part::Box", "Cube")
        obj.Length = size
        obj.Width = size
        obj.Height = size
        doc.recompute()
        FreeCADGui.activeView().viewAxonometric()
        return obj

    box_match = re.match(r"box\s+(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)", text)
    if box_match:
        l, w, h = map(float, box_match.groups())
        obj = doc.addObject("Part::Box", "Box")
        obj.Length = l
        obj.Width = w
        obj.Height = h
        doc.recompute()
        FreeCADGui.activeView().viewAxonometric()
        return obj

    cyl_match = re.match(r"cylinder\s+(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)", text)
    if cyl_match:
        r, h = map(float, cyl_match.groups())
        obj = doc.addObject("Part::Cylinder", "Cylinder")
        obj.Radius = r
        obj.Height = h
        doc.recompute()
        FreeCADGui.activeView().viewAxonometric()
        return obj

    raise ValueError("Unsupported instruction: {}".format(text))
