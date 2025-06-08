import FreeCAD
import FreeCADGui
from FreeCAD import Base
import re


def generate_from_text(text):

    """Generate or edit geometry from text instructions.

    Supported commands:
    - ``cube <length>`` -> create a cube
    - ``box <l> <w> <h>`` -> create a box
    - ``cylinder <radius> <height>`` -> create a cylinder
    - ``open <path>`` -> open a FreeCAD document
    - ``save <path>`` -> save the active document
    - ``translate <name> <x> <y> <z>`` -> move an object
    - ``scale <name> <factor>`` -> uniformly scale an object

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

    open_match = re.match(r"open\s+(.+)", text)
    if open_match:
        path = open_match.group(1).strip()
        opened = FreeCAD.openDocument(path)
        FreeCAD.setActiveDocument(opened.Name)
        FreeCADGui.activeDocument().activeView().viewAxonometric()
        return opened

    save_match = re.match(r"save\s+(.+)", text)
    if save_match:
        path = save_match.group(1).strip()
        if doc is None:
            raise ValueError("No active document to save")
        doc.saveAs(path)
        return doc

    trans_match = re.match(r"translate\s+(\w+)\s+(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)", text)
    if trans_match:
        name, dx, dy, dz = trans_match.groups()
        obj = doc.getObject(name)
        if obj is None:
            raise ValueError(f"Object {name} not found")
        vec = Base.Vector(float(dx), float(dy), float(dz))
        obj.Placement.Base = obj.Placement.Base.add(vec)
        doc.recompute()
        return obj

    scale_match = re.match(r"scale\s+(\w+)\s+(\d+(?:\.\d+)?)", text)
    if scale_match:
        name, factor = scale_match.groups()
        obj = doc.getObject(name)
        if obj is None:
            raise ValueError(f"Object {name} not found")
        factor = float(factor)
        if hasattr(obj, "Length"):
            obj.Length = float(obj.Length) * factor
        if hasattr(obj, "Width"):
            obj.Width = float(obj.Width) * factor
        if hasattr(obj, "Height"):
            obj.Height = float(obj.Height) * factor
        if hasattr(obj, "Radius"):
            obj.Radius = float(obj.Radius) * factor
        doc.recompute()
        return obj


    raise ValueError("Unsupported instruction: {}".format(text))

