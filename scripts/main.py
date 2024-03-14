#script.main.py

import sys
import os

# Determine the path to the root directory
root_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the root directory to sys.path
if root_directory not in sys.path:
    sys.path.append(root_directory)

# Import the run_gui function
from src.gui.main_gui import run_gui

if __name__ == "__main__":
    run_gui()
