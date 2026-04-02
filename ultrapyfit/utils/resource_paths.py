import sys
import os

def get_resource_path(relative_path):
    """
    Get the absolute path to a resource.
    Works for standard development and for PyInstaller bundled executables.
    """
    try:
        # PyInstaller creates a temp folder and stores its path in sys._MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # If sys._MEIPASS doesn't exist, we are running in normal Python mode.
        # Use the current working directory or the directory of the main script.
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)