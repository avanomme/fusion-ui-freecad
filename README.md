# Fusion360 UI for FreeCAD

This plugin transforms FreeCAD's interface to match Fusion 360's look and feel, including:
- Fusion 360-style interface layout
- Matching keyboard shortcuts
- Similar toolbar organization
- Fusion 360-inspired icons

## Installation

1. Clone this repository into your FreeCAD Mod directory:
   ```
   git clone [repository-url] ~/.FreeCAD/Mod/FusionUI
   ```

2. Restart FreeCAD

3. Enable the plugin in FreeCAD's preferences

## Features

- Fusion 360-style ribbon interface
- Matching keyboard shortcuts
- Customizable toolbar layouts
- Dark/Light theme support
- Icon replacement system

- Experimental AI-assisted design (text to geometry)
## Development

This plugin is built using:
- Python 3.x
- FreeCAD's Python API
- Qt for UI customization
- Custom icon resources

## Contributing

Contributions are welcome! Please follow the standard GitHub workflow:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT License 
## AI Assisted Design

Use the **AI Design** button to drive basic modeling commands from text.
Examples:

- ``cube 10`` – create a 10 mm cube
- ``box 5 8 2`` – create a box
- ``cylinder 4 12`` – create a cylinder
- ``open /path/to/file.FCStd`` – load a document
- ``save /path/to/out.FCStd`` – save the current document
- ``translate Cube 1 0 0`` – move an object by name
- ``scale Cube 2`` – scale an object

These commands demonstrate how text input can open, modify and generate
geometry directly in FreeCAD.

