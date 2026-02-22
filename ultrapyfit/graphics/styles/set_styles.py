"""
Modernized ultrapyfit style handler.
Refactored to support modern Matplotlib (>3.8) and Python (>3.9) standards.
"""
from pathlib import Path
import re
import json
from functools import wraps
import inspect
import matplotlib.pyplot as plt
import matplotlib.style as mpl_style

# Depending on the Matplotlib version, internal core functions vary.
# We import it this way to safely access style parsers.
import matplotlib.style.core as mpl_style_core

from ultrapyfit.graphics.styles.plot_base_functions import *

# Modern path resolution using pathlib
UTF_STYLE_DIR = Path(__file__).resolve().parent
UTF_BASIC_STYLES = UTF_STYLE_DIR / 'basic_styles'
STYLE_EXTENSION = 'mplstyle'
STYLE_FILE_PATTERN = re.compile(rf'([\S]+)\.{STYLE_EXTENSION}$')

# ==========================================
# 1. LOAD MATPLOTLIB LIBRARIES SAFELY
# ==========================================
# In modern Matplotlib, mpl_style.library contains all base and user styles.
library = dict(mpl_style.library)

# Safely load the custom ultrapyfit basic styles if the directory exists
if UTF_BASIC_STYLES.exists():
    try:
        utf_styles = mpl_style_core.read_style_directory(str(UTF_BASIC_STYLES))
        library.update(utf_styles)
    except AttributeError:
        print("Warning: Matplotlib version unsupported for custom style directory parsing.")


def check_if_valid_style(name: str) -> bool:
    """
    Return True if the name passed is available in the combined style library.
    """
    return name in library


def get_combined_style(styles):
    """
    Combines several matplotlib styles into a single dictionary.

    Parameters
    ----------
    styles: list or str
        List containing the names of the matplotlib styles to be combined,
        or a single string.
    """
    if isinstance(styles, str):
        if check_if_valid_style(styles):
            return library[styles]
        elif isinstance(styles, (str, Path)):
            return styles
        else:
            raise ValueError(f"Not a valid ultrapyfit style: {styles}")
    else:
        # Combine multiple styles by merging their dictionaries
        valid_styles = [library[i] for i in styles if check_if_valid_style(i)]
        if valid_styles:
            combined_style = {}
            for d in valid_styles:
                combined_style.update(d)
            return combined_style
        return None


# ==========================================
# 2. STYLE RESOLUTION CLASSES
# ==========================================
class FigureStyle:
    def __init__(self, name: str):
        self.name = name

    def get_style(self):
        raise NotImplementedError("Subclasses must implement get_style")


class MplFigureStyle(FigureStyle):
    def get_style(self):
        if check_if_valid_style(self.name):
            return library[self.name], None, None
        return None


class UtfFigureStyle(FigureStyle):
    def get_style(self):
        data = self._get_file()
        if data is not None:
            styles = data.get("styles", [])
            style = get_combined_style(styles)
            funct, funct_arg = self._get_utf_style_function(data)
            return style, funct, funct_arg
        return None

    def _get_file(self):
        """Scans the directory for a matching JSON style definition."""
        if not UTF_STYLE_DIR.exists():
            return None

        for file_path in UTF_STYLE_DIR.glob('*.json'):
            if self.name in file_path.name or file_path.stem == self.name:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if "utf_style" in data:
                            return data
                except Exception as e:
                    print(f"Error reading style file {file_path}: {e}")
                    continue
        return None

    def _get_utf_style_function(self, data):
        funct = data.get("function")
        funct_arg = data.get("function_arguments")
        return funct, funct_arg


def get_global_style(style_name: str):
    """Retrieves the style dictionary and post-processing functions."""
    style_data = MplFigureStyle(style_name).get_style()

    if style_data is None:
        style_data = UtfFigureStyle(style_name).get_style()

    if style_data is None:
        raise ValueError(f"Not a valid matplotlib or utf style: '{style_name}'")

    return style_data


# ==========================================
# 3. THE DECORATOR
# ==========================================
def use_style(func):
    """
    Decorator that changes the matplotlib style context dynamically
    before plotting, and applies post-processing if defined.
    """
    # Use inspect.signature (modern Python) instead of __code__.co_varnames
    sig = inspect.signature(func)

    @wraps(func)
    def style_func(*args, **kwargs):
        # Bind the arguments to see what the user passed
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        # If the function doesn't take a 'style' argument, just run it
        if 'style' not in bound_args.arguments:
            return func(*args, **kwargs)

        style_name = bound_args.arguments['style']

        # If style is None or empty, just run without applying anything
        if not style_name:
            return func(*args, **kwargs)

        # 1. Attempt to resolve the style
        try:
            style_dict, func_plot, func_plot_arg = get_global_style(style_name)
        except Exception as e:
            print(f"WARNING: Style resolution failed: {e}")
            print('Proceeding without applying custom style.')
            return func(*args, **kwargs)

        # 2. Setup arguments for the wrapped function
        # Mimic original behavior: if 'style' was in kwargs, remove it
        kwargs_to_pass = dict(kwargs)
        if 'style' in kwargs_to_pass:
            kwargs_to_pass.pop('style')

        res = None

        # 3. Apply the Context and Execute
        try:
            with plt.style.context(style_dict):
                res = func(*args, **kwargs_to_pass)
        except Exception as e:
            print(f"WARNING: Exception occurred while plotting with style: {e}")
            # Fallback to plotting without the context if it fails
            res = func(*args, **kwargs_to_pass)

        # 4. Apply post-processing function (from plot_base_functions)
        if func_plot is not None:
            # Look up the function by its string name in the global scope
            real_func_plot = globals().get(func_plot)
            if callable(real_func_plot):
                try:
                    if func_plot_arg is not None:
                        real_func_plot(func_plot_arg)
                    else:
                        real_func_plot()
                except Exception as e:
                    print(f"Failed to apply post-plot style function '{func_plot}': {e}")
            else:
                print(f"Style function '{func_plot}' is not defined or callable.")

        return res

    return style_func