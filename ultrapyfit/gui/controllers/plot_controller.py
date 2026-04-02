import re
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import SpanSelector
from pathlib import Path
from PySide6 import QtWidgets
from PySide6.QtCore import Qt


class PlotController:
    def __init__(self, main_window):
        self.mw = main_window
        self._drawn_scatter_pts = None

    def reset_3d_camera(self):
        """Forces the 3D view to redraw from scratch, clearing zoom and rotation."""
        if self.mw.treeExperiment.currentItem() is None:
            return
        self.plot_current_data_3D(reset_camera=True)

    def plot_current_data_3D(self, *args, reset_camera=False):
        if self.mw.treeExperiment.currentItem() is None:
            return
        if getattr(self.mw, '_is_loading_settings', False):
            return
        saved_state = None
        current_elev = 30
        current_azim = -60
        experiment = self.mw.get_experiment()
        current_fig = self.mw.mplWidget.canvas.figure
        if not reset_camera and current_fig.axes:
            old_ax = current_fig.axes[0]
            if hasattr(old_ax, 'elev') and hasattr(old_ax, 'azim'):
                saved_state = {
                    'elev': old_ax.elev,
                    'azim': old_ax.azim,
                    'roll': getattr(old_ax, 'roll', 0),
                    'zoom_level': getattr(old_ax, '_custom_zoom_level', 0.85)
                }
        cmap, stride, plot_type = self.get_3D_options()
        plot_type = self.mw.viewStyleDict3D.get(plot_type)
        fig, ax = experiment.plot_3D(cmap=cmap, plot_type=plot_type, stride=stride, azim=current_azim,
                                     elev=current_elev)
        if saved_state:
            ax.view_init(
                elev=saved_state['elev'],
                azim=saved_state['azim'],
                roll=saved_state['roll']
            )
            ax._custom_zoom_level = saved_state['zoom_level']
            current_aspect = ax.get_box_aspect()
            ax.set_box_aspect(current_aspect, zoom=saved_state['zoom_level'])
        self.enable_scroll_zoom(ax)
        self.mw.mplWidget.update_figure(fig)
        plt.close(fig)
        self.mw.settings_manager._save_current_dataset_settings()

    def get_3D_options(self):
        return self.mw.cbColormaps3D.currentText().lower(), 11 - self.mw.sbRenderQuality3D.value(), self.mw.cbStyle3D.currentText()

    def plot_current_data_spectrum(self):
        if self.mw.treeExperiment.currentItem() is None:
            return
        if getattr(self.mw, '_is_loading_settings', False):
            return
        experiment = self.mw.get_experiment()
        times_arg, rango_arg, cover_arg, legend_arg = self.get_spectrum_options()
        fig, ax = experiment.plot_spectra(
            times=times_arg,
            rango=rango_arg,
            average=self.mw.sbAverageSpectra.value(),
            cover_range=cover_arg,
            from_max_to_min=self.mw.chkFromMaxToMinSpectra.isChecked(),
            legend=legend_arg,
            cmap=self.mw.cbColormapsSpectra.currentText().lower() or None,
            style=self.mw.viewStyleDictSpectral.get(self.mw.cbStyleSpectra.currentText()),
        )
        self.enable_interactive_features(fig, ax, experiment.wavelength, target_lineedit=self.mw.leCustomWavelengthTrace)
        fig.tight_layout()
        self.mw.mplWidget.update_figure(fig)
        plt.close(fig)
        self.mw.settings_manager._save_current_dataset_settings()

    def get_spectrum_options(self):
        times_arg = 'all'
        if self.mw.rbAutomaticSpectra.isChecked():
            n_spec = self.mw.sbNumberOfSpectra.value()
            if self.mw.chkAtWavelengthSpectra.isChecked():
                wl = self.mw.dsbAtWavelengthSpectra.value()
                times_arg = ["auto", n_spec, wl]
            else:
                times_arg = ["auto", n_spec]

        elif self.mw.rbCustomSpectra.isChecked():
            text = self.mw.leCustomTimesSpectral.text()
            try:
                times_arg = [float(x.strip()) for x in text.split(',') if x.strip()]
            except ValueError:
                times_arg = 'auto'

        rango_arg = None
        if self.mw.chkTimeRangeSpectra.isChecked():
            rango_arg = [self.mw.dsbTimeRangeStartSpectra.value(), self.mw.dsbTimeRangeStopSpectra.value()]

        cover_arg = None
        if self.mw.chkMaskRangeSpectra.isChecked():
            cover_arg = [self.mw.dsbMaskRangeStartSpectra.value(),
                         self.mw.dsbMaskRangeStopSpectra.value()]

        index = self.mw.cbLegendSpectra.currentIndex()
        if index == 0:
            legend_arg = True
        elif index == 1:
            legend_arg = "bar"
        else:
            legend_arg = False
        return times_arg, rango_arg, cover_arg, legend_arg

    def plot_current_data_traces(self):
        if self.mw.treeExperiment.currentItem() is None:
            return
        if getattr(self.mw, '_is_loading_settings', False):
            return
        experiment = self.mw.get_experiment()
        traces_val, legend_val, style_val = self.get_trace_options()
        fig, ax = experiment.plot_traces(traces=traces_val,
                                         style=style_val,
                                         legend=legend_val)
        self.enable_interactive_features(fig, ax, experiment.time, target_lineedit=self.mw.leCustomTimesSpectral)
        fig.tight_layout()
        self.mw.mplWidget.update_figure(fig)
        plt.close(fig)
        self.mw.settings_manager._save_current_dataset_settings()

    def get_trace_options(self):
        experiment = self.mw.get_experiment()
        if self.mw.rbAllTrace.isChecked():
            traces_val = experiment.wavelength.tolist()
        elif self.mw.rbAutomaticTrace.isChecked():
            traces_val = "auto"
        else:
            raw_text = self.mw.leCustomWavelengthTrace.text()
            clean_text = raw_text.replace(';', ',')
            try:
                traces_val = [float(x.strip()) for x in clean_text.split(',') if x.strip()]
                if not traces_val:
                    traces_val = "auto"
            except ValueError:
                traces_val = "auto"
        legend_text = self.mw.cbLegendTrace.currentIndex()
        if legend_text == 1:
            legend_val = True
        elif legend_text == 2:
            legend_val = False
        else:
            legend_val = 'auto'
        style_text = self.mw.cbStyleTrace.currentText()
        style_val = self.mw.viewStyleDictTrace.get(style_text)
        return traces_val, legend_val, style_val

    def plot_current_data_svd(self):
        if self.mw.treeExperiment.currentItem() is None:
            return
        if getattr(self.mw, '_is_loading_settings', False):
            return
        experiment = self.mw.get_experiment()
        calc_comps, show_comps, log_scale = self.mw.svd_controller.get_svd_parameters()

        if not hasattr(experiment, '_S') or experiment._S is None or len(experiment._S) < show_comps:
            self.mw.svd_controller.update_svd_math()
            return

        fig, axes = experiment.plot_full_svd(components=show_comps, log_scale=log_scale)
        fig.tight_layout()
        self.mw.svdMplWidget.update_figure(fig)
        plt.close(fig)
        self.mw.settings_manager._save_current_dataset_settings()

    def plot_current_data_fit_preview(self):
        if self.mw.treeExperiment.currentItem() is None:
            return
        if getattr(self.mw, '_is_loading_settings', False):
            return
        experiment = self.mw.get_experiment()
        params = self.mw.fitting_controller.get_fit_parameters()
        (fit_mode, data_sel_type, svd_comps, traces_list, average,
         region_min, region_max, single_wave, single_average, mask_list,
         exp_no, irf_w, irf_mu, initial_taus, tau_inf) = params

        if fit_mode == 0:
            if data_sel_type == 'svd':
                experiment.select_SVD_vectors(val=svd_comps)
            elif data_sel_type == 'traces' and traces_list:
                experiment.select_traces(points=traces_list, average=average, avoid_regions=mask_list)
            elif data_sel_type == 'region':
                experiment.select_region(mini=region_min, maxi=region_max)
        elif fit_mode == 1:
            experiment.select_traces(points=[single_wave], average=single_average)

        fig, ax = experiment.plot_traces(traces='select', legend='auto')
        fig.tight_layout()
        self.mw.fittingPreviewMplWidget.update_figure(fig)
        plt.close(fig)
        self.mw.settings_manager._save_current_dataset_settings()

    def plot_current_data_global_fit(self):
        current_item = self.mw.treeExperiment.currentItem()
        if not current_item:
            return
        if getattr(self.mw, '_is_loading_settings', False):
            return
        node_data = current_item.data(0, Qt.UserRole)
        experiment = self.mw.get_experiment()
        if not experiment or not isinstance(node_data, dict):
            return
        fit_number = node_data.get('fit_number')
        view_mode = self.mw.cbGlobalViewMode.currentIndex()

        try:
            if view_mode == 0:
                do_eas = self.mw.chkConvertToEAS.isChecked()
                fig, ax = experiment.fitting.plot_DAS(fit_number=fit_number, convert_to_EAS=do_eas, plot_offset=True, number='all')
            elif view_mode in [1, 2]:
                selection_text = self.mw.leGlobalKineticsSel.text().strip()
                trace_selection = None
                if selection_text:
                    matches = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", selection_text)
                    if matches:
                        trace_selection = [float(x) for x in matches]
                wants_residues = (view_mode == 2)
                fig, ax = experiment.fitting.plot_global_fit(fit_number=fit_number, selection=trace_selection, plot_residues=wants_residues)
            fig.tight_layout()
            self.mw.globalMplWidget.update_figure(fig)
            plt.close(fig)
        except Exception as e:
            self._clear_plot_with_message(self.mw.globalMplWidget, f"Error during plotting:\n{str(e)}")
        self.mw.fitting_controller._update_fit_text_report(experiment, fit_number, self.mw.textGlobalReport)

    def plot_current_data_single_fit(self):
        current_item = self.mw.treeExperiment.currentItem()
        if not current_item:
            return
        if getattr(self.mw, '_is_loading_settings', False):
            return
        node_data = current_item.data(0, Qt.UserRole)
        experiment = self.mw.get_experiment()
        if not experiment or not isinstance(node_data, dict):
            return
        fit_number = node_data.get('fit_number')
        show_details = self.mw.chkSingleDetails.isChecked()
        try:
            fig, ax = experiment.fitting.plot_single_fit(fit_number=fit_number, details=show_details)
            fig.tight_layout()
            self.mw.singleMplWidget.update_figure(fig)
            plt.close(fig)
        except Exception as e:
            self._clear_plot_with_message(self.mw.singleMplWidget, f"Error during plotting:\n{str(e)}")

    def export_plot(self):
        file_filters = "Portable Document Format (*.pdf);;Scalable Vector Graphics (*.svg);;Portable Network Graphics (*.png);;Encapsulated PostScript (*.eps);;Tagged Image File Format (*.tif);;All Files (*)"
        file_path, selected_filter = QtWidgets.QFileDialog.getSaveFileName(self.mw, "Export Plot As", "", file_filters)
        if not file_path:
            return
        self.mw.statusbar.showMessage(f"Exporting to {file_path}...")
        path_obj = Path(file_path)
        extension = path_obj.suffix.lower()
        if not extension and selected_filter != "All Files (*)":
            match = re.search(r'\*\.([a-zA-Z0-9]+)', selected_filter)
            if match:
                extension = f".{match.group(1).lower()}"
                file_path += extension
        self.save_matplotlib_figure(file_path)
        self.mw.statusbar.showMessage(f"Successfully exported: {file_path}", 5000)

    def save_matplotlib_figure(self, path):
        experiment = self.mw.get_experiment()
        if self.mw.cbViewMode.currentIndex() == 0:
            current_fig = self.mw.mplWidget.canvas.figure
            old_ax = current_fig.axes[0]
            saved_state = {'elev': old_ax.elev, 'azim': old_ax.azim, 'roll': getattr(old_ax, 'roll', 0), 'zoom_level': getattr(old_ax, '_custom_zoom_level', 0.85)}
            cmap, stride, plot_type = self.get_3D_options()
            plot_type = self.mw.viewStyleDict3D.get(plot_type)
            fig, ax = experiment.plot_3D(cmap=cmap, figsize=(8, 6), plot_type=plot_type, stride=stride, azim=old_ax.azim, elev=old_ax.elev)
            ax.view_init(elev=saved_state['elev'], azim=saved_state['azim'], roll=saved_state['roll'])
            ax._custom_zoom_level = saved_state['zoom_level']
            current_aspect = ax.get_box_aspect()
            ax.set_box_aspect(current_aspect, zoom=saved_state['zoom_level'])
        elif self.mw.cbViewMode.currentIndex() == 1:
            times_arg, rango_arg, cover_arg, legend_arg = self.get_spectrum_options()
            style = self.mw.viewStyleDictSpectral.get(self.mw.cbStyleSpectra.currentText())
            if style == "lmu_spec_gui": style = "lmu_spec"
            elif style == "lmu_specd_gui": style = "lmu_specd"
            fig, ax = experiment.plot_spectra(times=times_arg, rango=rango_arg, average=self.mw.sbAverageSpectra.value(), cover_range=cover_arg, from_max_to_min=self.mw.chkFromMaxToMinSpectra.isChecked(), legend=legend_arg, cmap=self.mw.cbColormapsSpectra.currentText().lower() or None, style=style)
        else:
            traces_val, legend_val, style_val = self.get_trace_options()
            if style_val == "lmu_trac_gui": style_val = "lmu_trac"
            elif style_val == "lmu_tracd_gui": style_val = "lmu_tracd"
            fig, ax = experiment.plot_traces(traces=traces_val, style=style_val, legend=legend_val)
        fig.savefig(path, dpi=600, bbox_inches='tight', pad_inches=0.05, transparent=False, facecolor='w', edgecolor='w')
        plt.close(fig)

    def _clear_plot_with_message(self, widget, message):
        fig = widget.canvas.figure
        fig.clear()
        ax = fig.add_subplot(111)
        ax.axis('off')
        ax.text(0.5, 0.5, message, horizontalalignment='center', verticalalignment='center', fontsize=12, color='gray')
        widget.canvas.draw()

    def enable_scroll_zoom(self, ax):
        ax._custom_zoom_level = getattr(ax, '_custom_zoom_level', 1.0)
        def on_scroll(event):
            if event.inaxes != ax: return
            zoom_multiplier = 1.1 if event.button == 'up' else 0.9
            ax._custom_zoom_level *= zoom_multiplier
            current_aspect = ax.get_box_aspect()
            ax.set_box_aspect(current_aspect, zoom=ax._custom_zoom_level)
            ax.figure.canvas.draw_idle()
        self.mw._scroll_cid = ax.figure.canvas.mpl_connect('scroll_event', on_scroll)

    def enable_interactive_features(self, fig, ax, x_data, target_lineedit=None):
        if not hasattr(self, '_drawn_interactive_lines'): self._drawn_interactive_lines = []
        def sync_red_lines(vals):
            for line in self._drawn_interactive_lines:
                try: line.remove()
                except ValueError: pass
            self._drawn_interactive_lines.clear()
            for val in vals:
                line = ax.axvline(val, color='red', linestyle=':', alpha=0.6, zorder=1)
                self._drawn_interactive_lines.append(line)
            fig.canvas.draw_idle()
        def on_click(event):
            if event.inaxes != ax or target_lineedit is None: return
            if event.button not in [1, 3]: return
            current_text = target_lineedit.text()
            current_vals = [float(x.strip()) for x in current_text.replace(';', ',').split(',') if x.strip()]
            if event.button == 1:
                idx = np.argmin(np.abs(x_data - event.xdata))
                clicked_val = x_data[idx]
                if clicked_val not in current_vals:
                    current_vals.append(clicked_val)
                    current_vals.sort()
                    target_lineedit.setText(", ".join([f"{v:.1f}" for v in current_vals]))
                    sync_red_lines(current_vals)
            elif event.button == 3:
                if not current_vals: return
                current_vals_array = np.array(current_vals)
                closest_idx = np.argmin(np.abs(current_vals_array - event.xdata))
                closest_val = current_vals[closest_idx]
                click_px = ax.transData.transform((event.xdata, 0))
                line_px = ax.transData.transform((closest_val, 0))
                pixel_distance = abs(click_px[0] - line_px[0])
                if pixel_distance <= 15.0:
                    current_vals.pop(closest_idx)
                    target_lineedit.setText(", ".join([f"{v:.1f}" for v in current_vals]))
                    sync_red_lines(current_vals)
        self.mw._cid_click = fig.canvas.mpl_connect('button_press_event', on_click)
        if target_lineedit:
            initial_text = target_lineedit.text()
            initial_vals = [float(x.strip()) for x in initial_text.replace(';', ',').split(',') if x.strip()]
            if initial_vals: sync_red_lines(initial_vals)

    def enable_2d_point_picking(self, fig, ax, target_lineedit=None):
        self._chirp_2d_points = []
        if hasattr(self, '_drawn_scatter_pts') and self._drawn_scatter_pts is not None:
            try: self._drawn_scatter_pts.remove()
            except ValueError: pass
        self._drawn_scatter_pts = None
        def sync_scatter():
            if self._drawn_scatter_pts is not None:
                try: self._drawn_scatter_pts.remove()
                except ValueError: pass
            if self._chirp_2d_points:
                xs = [p[0] for p in self._chirp_2d_points]; ys = [p[1] for p in self._chirp_2d_points]
                self._drawn_scatter_pts = ax.scatter(xs, ys, color='red', edgecolors='black', s=40, zorder=10)
            else: self._drawn_scatter_pts = None
            fig.canvas.draw_idle()
        def on_click(event):
            if event.inaxes != ax or target_lineedit is None: return
            toolbar = getattr(fig.canvas.manager, 'toolbar', None) if fig.canvas.manager else None
            if toolbar and toolbar.mode != '': return
            click_x, click_y = event.xdata, event.ydata
            if event.button == 1:
                self._chirp_2d_points.append((click_x, click_y))
                self._chirp_2d_points.sort(key=lambda p: p[0])
                target_lineedit.setText(", ".join([f"{x:.1f}:{y:.3f}" for x, y in self._chirp_2d_points]))
                sync_scatter()
            elif event.button == 3:
                if not self._chirp_2d_points: return
                click_px = ax.transData.transform((click_x, click_y))
                min_dist = float('inf'); closest_idx = -1
                for i, (px, py) in enumerate(self._chirp_2d_points):
                    pt_px = ax.transData.transform((px, py))
                    dist = np.hypot(click_px[0] - pt_px[0], click_px[1] - pt_px[1])
                    if dist < min_dist: min_dist, closest_idx = dist, i
                if min_dist <= 15.0 and closest_idx != -1:
                    self._chirp_2d_points.pop(closest_idx)
                    target_lineedit.setText(", ".join([f"{x:.1f}:{y:.3f}" for x, y in self._chirp_2d_points]))
                    sync_scatter()
        return fig.canvas.mpl_connect('button_press_event', on_click)

    def enable_range_picking(self, ax, le_min, le_max):
        def on_select(vmin, vmax):
            if le_min: le_min.setText(f"{vmin:.2f}")
            if le_max: le_max.setText(f"{vmax:.2f}")
        return SpanSelector(ax, on_select, direction='horizontal', useblit=True, props=dict(alpha=0.2, facecolor='red'), interactive=True)
