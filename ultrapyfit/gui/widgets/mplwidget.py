from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class MplWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Start with a blank placeholder
        self.canvas = None
        self._create_placeholder()

    def _create_placeholder(self):
        """Creates an empty starting canvas."""
        fig = Figure(figsize=(6, 5), dpi=100)
        ax = fig.add_subplot(111)
        ax.text(0.5, 0.5, "No Data Loaded", ha='center', va='center')
        self.update_figure(fig)

    def update_figure(self, new_fig):
        """
        Takes a generated Figure (e.g., from plot_3D),
        destroys the old canvas, and embeds the new one.
        """
        # 1. Safely remove and destroy the old canvas to prevent memory leaks
        if self.canvas is not None:
            self.layout.removeWidget(self.canvas)
            self.canvas.close()
            self.canvas.deleteLater()

        # 2. Wrap the library's Figure in a Qt Canvas
        self.canvas = FigureCanvas(new_fig)

        # 3. Insert it into the GUI layout
        self.layout.addWidget(self.canvas)

        # 4. Force a redraw
        self.canvas.draw()
