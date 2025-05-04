#!/bin/bash

# Run this inside FusionWorkbench directory
mkdir -p \
  resources/icons \
  resources/translations \
  core \
  layout \
  ui \
  features/solid \
  features/mesh \
  features/surface \
  commands \
  utils \
  tests

# Create __init__.py files in all packages
find . -type d \( ! -path . \) -exec touch {}/__init__.py \;

# Core files
touch core/{toolbar.py,workspace_state.py,mode_switcher.py}

# Layout files
touch layout/{main_panel.py,toolbar_solid.py,toolbar_mesh.py}

# UI shared components
touch ui/{shortcut_bar.py,dropdown_bar.py,shortcut_button.py,dropdown_button.py}

# Feature-specific logic
touch features/solid/{shortcuts.py,dropdown.py}
touch features/mesh/{shortcuts.py,dropdown.py}
touch features/surface/{shortcuts.py,dropdown.py}

# Command implementations
touch commands/{cmd_extrude.py,cmd_revolve.py,cmd_shell.py}

# Utils
touch utils/{icon_loader.py,file_utils.py,qdialog_utils.py}

# Tests
touch tests/{test_shortcut_buttons.py,test_toolbar_assembly.py}

# FreeCAD entry files
touch InitGui.py fusion_workbench.py