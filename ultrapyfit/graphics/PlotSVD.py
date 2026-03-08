# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 11:29:27 2020

@author: lucas
"""
from scipy.sparse.linalg import svds as svd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.widgets import Slider, Button
from ultrapyfit.utils.divers import select_traces
from copy import copy
from ultrapyfit.graphics.styles.set_styles import *
from ultrapyfit.graphics.styles.plot_base_functions import *


class PlotSVD:
    """
    Class to do a singular value decomposition (SVD) of the data and explore
    the results.

    Attributes
    ----------
    x: 1darray
        x-vector, normally time vector

    data: 2darray
        array containing the data, the number of rows should be equal to
        the len(x)

    wavelength: 1darray
        wavelength vector

    selected_traces: 2darray
        sub dataset of data

    selected_wavelength: 1darray
        sub dataset of wavelength

    _S:
        Number of singular values calculated.

    _U:
        Number of left singular vectors calculated  .

    _V:
        Number of right singular vectors calculated.
    """

    def __init__(self, x, data, wavelength, selected_traces=None,
                 selected_wavelength=None):
        self.data = data
        self.x = x
        self.wavelength = wavelength
        self.selected_traces = selected_traces
        self.selected_wavelength = selected_wavelength
        self._SVD_fit = False
        self._U, self._S, self._V = self._calculateSVD()
        self._fig = None
        self._ax = None
        self._number_of_vectors_plot = None
        self._specSVD = None
        self._button_svd_select = None
        self._vertical_line_SVD = None

    def get_svd_decomposition(self):
        """
        Return the left singular vectors(U) the eingen values(S) and right
        singular vectors(V).
        """
        return self._U, self._S, self._V

    def _calculateSVD(self, vectors=15):
        """
        Calculated a truncated SVD of the data matrix using
        scipy.sparse.linalg.svd function

        Parameters
        ----------
        vectors:
            number of singular values and singular vectors to be calculated
        """
        u, s, v = svd(self.data, k=vectors)
        return u[:, ::-1], s[::-1], v[::-1, :]

    def calculate_svd(self, n_components=15):
        """
        Calculates the Singular Value Decomposition (SVD) of the data and
        securely stores the U, S, and V matrices internally.

        Parameters
        ----------
        n_components : int, optional
            Number of singular vectors to calculate. Default is 15.
        """
        from scipy.sparse.linalg import svds

        # scipy svds requires k to be strictly less than the minimum dimension
        max_components = min(self.data.shape) - 1
        n_components = min(n_components, max_components)

        u, s, v = svd(self.data, k=n_components)

        # Update internal state safely (Encapsulation)
        self._U = u
        self._S = s
        self._V = v

    def plot_full_svd(self, components=3, log_scale=True):
        """
        Plots the full SVD results: Scree plot, Kinetics (Left Singular Vectors),
        and Spectra (Right Singular Vectors).

        Parameters
        ----------
        components : int, optional
            Number of components to plot. The default is 3.
        log_scale : bool, optional
            Whether to use a logarithmic y-axis for the singular values (Scree plot).
            Default is True.

        Returns
        -------
        fig : matplotlib.figure.Figure
        axes : numpy.ndarray of matplotlib.axes.Axes
        """

        # Create a new figure (similar to plot_traces / plot_spectra)
        fig = plt.figure(figsize=(10, 8))

        # Save to self._fig so that other internal methods (like cursors or
        # export functions) can find it if needed.
        self._fig = fig

        # Create subplots: Top full width for Scree, Bottom for Kinetics & Spectra
        ax_scree = fig.add_subplot(2, 1, 1)
        ax_kin = fig.add_subplot(2, 2, 3)
        ax_spec = fig.add_subplot(2, 2, 4)
        axes = np.array([ax_scree, ax_kin, ax_spec])

        # SVD from scipy.sparse.linalg.svds returns ascending singular values.
        # Check if we need to reverse them to be descending for correct plotting.
        if hasattr(self, '_S') and self._S is not None:
            if len(self._S) > 1 and self._S[0] < self._S[-1]:
                s = self._S[::-1]
                u = self._U[:, ::-1] if hasattr(self, '_U') else None
                v = self._V[::-1, :] if hasattr(self, '_V') else None
            else:
                s = self._S
                u = self._U
                v = self._V

            # 1. Plot Scree
            ax_scree.plot(np.arange(1, len(s) + 1), s, 'ko-', markersize=5, label="Singular Values")
            ax_scree.plot(np.arange(1, components + 1), s[:components], 'ro', markersize=7, label="Selected")
            if log_scale:
                ax_scree.set_yscale('log')
                ax_scree.set_ylabel("Log(Singular Value)")
            else:
                ax_scree.set_yscale('linear')
                ax_scree.set_ylabel("Singular Value")

            ax_scree.set_title("Singular Values (Scree Plot)")
            ax_scree.set_xlabel("Component Index")
            ax_scree.grid(True, linestyle='--', alpha=0.6)
            ax_scree.legend()

            cmap = mpl.colormaps['tab10']

            # 2. Plot Kinetics (U)
            if u is not None:
                for i in range(min(components, u.shape[1])):
                    ax_kin.plot(self.x, u[:, i], label=f'Comp {i + 1}', color=cmap(i % 10))
            ax_kin.set_title("Left Singular Vectors (Kinetics)")
            ax_kin.set_xlabel("Time")
            ax_kin.set_ylabel("Amplitude")
            ax_kin.grid(True, linestyle='--', alpha=0.6)
            ax_kin.legend()

            # 3. Plot Spectra (V)
            if v is not None:
                for i in range(min(components, v.shape[0])):
                    ax_spec.plot(self.wavelength, v[i, :], label=f'Comp {i + 1}', color=cmap(i % 10))
            ax_spec.set_title("Right Singular Vectors (Spectra)")
            ax_spec.set_xlabel("Wavelength")
            ax_spec.set_ylabel("Amplitude")
            ax_spec.grid(True, linestyle='--', alpha=0.6)
            ax_spec.legend()

        return fig, axes

    def _close_svd_fig(self):
        """
        reestablish initial values after closing the svd plot. This is important
         since this object cannot be pickled
        """
        self._fig = None
        self._ax = None
        self._number_of_vectors_plot = None
        self._specSVD = None
        self._button_svd_select = None
        self._vertical_line_SVD = None

    @use_style
    def plot_singular_values(self, data='all', size=14, log_scale=True):
        """
        Plot the singular values of either the whole data set or the selected
        data set.

        Parameters
        ----------
        data: str "all" or "select"
            If "all" the singular values plotted correspond to the whole data
            set if "select" correspond to the singular values of the selected
            traces.

        size: int (default 14)
            size of the figure text labels including tick labels axis labels and
             legend.

        log_scale: bool (default True)
            defines the scale of the y axis, if true a logarithmic scale will
            be set.
        """

        if data == 'selected':
            dat = self.selected_traces
        else:
            dat = self.data
        svd_values = (np.linalg.svd(dat, full_matrices=False,
                                    compute_uv=False)) ** 2
        x = np.linspace(1, len(svd_values), len(svd_values))
        f, ax = plt.subplots(1)
        plt.plot(x, svd_values, marker='o', alpha=0.6, ms=4, ls='')
        plt.ylabel('Eigen values', size=size)
        plt.xlabel('number', size=size)
        plt.minorticks_on()
        ax.tick_params(which='both', direction='in', top=True, right=True,
                       labelsize=size)
        if log_scale:
            plt.yscale("log")
        return f, ax

    def _updatePlotSVD(self, val):
        """
        Function to update the SVD plot with the specSVD slider
        """
        wavelength = self.wavelength
        value = int(round(self._specSVD.val))
        colores = ['tab:orange', 'tab:green', 'tab:red', 'tab:purple',
                   'tab:brown',
                   'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan', 'tab:blue']
        if value > self._number_of_vectors_plot:
            if value + 1 == self._number_of_vectors_plot:
                value_c = value * 1.0
                if value > 10:
                    value_c = value - 10 * (value // 10)
                self._ax[0].plot(self.x, self._U[:, value],
                                 color=colores[value_c + 1])
                self._ax[2].plot(wavelength, self._V[value, :],
                                 color=colores[value_c + 1])
            else:
                for i in range(int(self._number_of_vectors_plot), int(value)):
                    value_c = i
                    if i > 10:
                        value_c = i - 10 * (value // 10)
                    self._ax[0].plot(self.x, self._U[:, i],
                                     color=colores[value_c - 1])
                    self._ax[2].plot(wavelength, self._V[i, :],
                                     color=colores[value_c - 1])
            self._vertical_line_SVD.remove()
            self._vertical_line_SVD = self._ax[1].axvline(value, alpha=0.5,
                                                          color='red',
                                                          zorder=np.inf)

            self._number_of_vectors_plot = value * 1.0
        elif value < self._number_of_vectors_plot:
            self._vertical_line_SVD.remove()
            self._vertical_line_SVD = self._ax[1].axvline(value, alpha=0.5,
                                                          color='red',
                                                          zorder=np.inf)

            for i in range(int(value), int(self._number_of_vectors_plot)):
                del self._ax[0].lines[-1]
                del self._ax[2].lines[-1]
            self._number_of_vectors_plot = value * 1.0
        else:
            pass
        self._fig.canvas.draw_idle()

    def select_SVD_vectors(self, val):
        """
        function to select the left singular vectors as selected traces.
        This allows to perform a fit to the singular vector which is much faster
         than a global fit, since the number of singular vector is lower.

        Parameters
        ----------
        val: int
            indicate the number of singular vectors to select
        """
        self.selected_traces = self._U[:, :val]
        self._SVD_fit = True
        self.selected_wavelength = np.linspace(1, val, val)

    def _selectSVD(self, val):
        """
        function to select the left singular vectors as selected traces from
        the SVD plot.
        """
        value = int(round(self._specSVD.val))
        self.select_SVD_vectors(value)
        plt.close(self._fig)
        self._close_svd_fig()

    def select_traces(self, points=10, average=1, avoid_regions=None):
        """
        Method to select traces from the data attribute ande defines a subset
        of traces in the selected_traces attribute

        Parameters
        ----------
        points: int or list or "auto" (default 10)
            If type(space) =int: a series of traces separated by the value
            indicated will be selected.
            If type(space) = list: the traces in the list will be selected.
            If space = auto, the number of returned traces is 10 and equally
            spaced along the wavelength vector and points is set to 0

        average: int (default 1)
            Binning points surrounding the selected wavelengths.
            e. g.: if point is 1 trace = mean(index-1, index, index+1)

        avoid_regions: list of list (default None)
            Defines wavelength regions that are avoided in the selection when
            space is an integer. The sub_list should have two elements defining
            the region to avoid in wavelength values
            i. e.: [[380,450],[520,530] traces with wavelength values between
                380-450 and 520-530 will not be selected
        """
        if points == 'all':
            self.selected_traces = copy(self.data)
            self.selected_wavelength = copy(self.wavelength)
        else:
            self.selected_traces, self.selected_wavelength = select_traces(
                self.data, self.wavelength, points,
                average, avoid_regions)
        self._SVD_fit = False
