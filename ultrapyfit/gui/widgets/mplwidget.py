from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy, QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.widgets import Cursor
from mpl_toolkits.mplot3d import Axes3D


class MplWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.toolbar = None
        self.canvas = None
        self._cursors = []  # Must keep references to cursors so they aren't garbage collected

        # Start with a blank placeholder
        self._create_placeholder()

    def _create_placeholder(self):
        """Creates an empty starting canvas."""
        fig = Figure(figsize=(6, 5), dpi=100)
        ax = fig.add_subplot(111)
        ax.axis('off')

        # Place text right in the middle
        ax.text(0.5, 0.5, "No experiments have been loaded.\nPlease select one from Project Explorer.",
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=12, color='gray')
        self.update_figure(fig)

    def update_figure(self, new_fig):
        """Destroys the old canvas and toolbar, embeds the new ones safely."""
        if self.canvas is not None:
            self.layout.removeWidget(self.canvas)
            self.canvas.close()
            self.canvas.deleteLater()

        if self.toolbar is not None:
            self.layout.removeWidget(self.toolbar)
            self.toolbar.close()
            self.toolbar.deleteLater()
            self.toolbar = None

        self.canvas = FigureCanvas(new_fig)

        # 2. Only add the standard toolbar if it's a 2D plot!
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.setStyleSheet("background-color: transparent; border: none;")

        self._setup_interactivity(new_fig)

        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)

        self.canvas.draw()

    def _setup_interactivity(self, fig):
        """Attaches fast crosshairs to all 2D subplots."""
        self._cursors.clear()

        for ax in fig.axes:
            # 3D plots crash the Cursor widget, so we skip them completely
            if isinstance(ax, Axes3D) or ax.name == '3d':
                continue

            # Create a fast-blitting crosshair for standard 2D plots
            cursor = Cursor(ax, useblit=True, color='gray', linewidth=1, linestyle='--')
            self._cursors.append(cursor)