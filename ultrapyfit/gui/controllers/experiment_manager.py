import uuid
import os
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from ultrapyfit.experiment import Experiment
from ultrapyfit.gui.windows.import_dialog import ImportDialog


class ExperimentManager:
    def __init__(self, main_window):
        self.mw = main_window
        self.experiments: dict[str, Experiment] = {}

    def open_import_dialog(self):
        """Open the parameter dialog and connect to its signals"""
        self.mw.import_dialog = ImportDialog(self.mw)
        self.mw.import_dialog.parameters_accepted.connect(self.on_experiment_received)
        self.mw.import_dialog.exec()

    def on_experiment_received(self, imported_experiment: Experiment) -> None:
        """Slot called when parameters_accepted signal is emitted"""
        self.add_experiment(imported_experiment)
        if self.mw.import_dialog.isVisible():
            self.mw.import_dialog.close()

    def save_experiment(self):
        """Save the currently selected experiment to an .exp file."""
        experiment = self.get_experiment()
        if not experiment:
            QtWidgets.QMessageBox.warning(self.mw, "No Selection", "Please select an experiment to save.")
            return

        default_name = experiment._data_path.split("/")[-1].split(".")[0] if experiment._data_path else "experiment"
        path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self.mw, "Save Experiment", f"{default_name}.exp", "Ultrapyfit Experiment (*.exp)"
        )

        if path:
            try:
                experiment.save(path)
                self.mw.statusBar().showMessage(f"Experiment saved to {path}", 5000)
            except Exception as e:
                QtWidgets.QMessageBox.critical(self.mw, "Error", f"Failed to save experiment:\n{str(e)}")

    def load_experiment(self):
        """Load an experiment from an .exp file."""
        path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self.mw, "Load Experiment", "", "Ultrapyfit Experiment (*.exp);;All Files (*)"
        )

        if path:
            try:
                loaded_exp = Experiment.load(path)
                if loaded_exp:
                    # Update data path to the .exp file location for display if original path is missing
                    if not loaded_exp._data_path:
                        loaded_exp._data_path = path
                    self.add_experiment(loaded_exp)
                    self.mw.statusBar().showMessage(f"Experiment loaded from {path}", 5000)
            except Exception as e:
                QtWidgets.QMessageBox.critical(self.mw, "Error", f"Failed to load experiment:\n{str(e)}")

    def add_experiment(self, experiment: Experiment):
        """Called when Import Window finishes or when an experiment is loaded."""
        exp_id = str(uuid.uuid4())
        self.experiments[exp_id] = experiment

        root_item = QtWidgets.QTreeWidgetItem(self.mw.treeExperiment)
        display_name = os.path.basename(experiment._data_path) if experiment._data_path else "Untitled Experiment"
        root_item.setText(0, display_name)
        root_item.setExpanded(True)
        root_item.setData(0, Qt.UserRole, exp_id)

        # Restore Fit nodes if they exist
        self._restore_fit_nodes(root_item, experiment)

        self.mw.dataset_settings[exp_id] = {}
        self.mw.settings_manager._load_dataset_settings()
        self.mw.treeExperiment.setCurrentItem(root_item)
        
        # Update UI state
        self.mw.preprocessing_controller.update_history_list()
        self.mw.preprocessing_controller.plot_preprocessing_preview()
        self.mw._enable_controls(True)
        self.mw.stackedViewModeOptions.setCurrentIndex(0)
        self.mw.cbViewMode.setCurrentIndex(0)

    def _restore_fit_nodes(self, root_item, experiment):
        """Re-creates the tree nodes for existing fits in a loaded experiment."""
        # Restore Global Fits
        for fit_num, result in experiment.fitting.fit_records.global_fits.items():
            exp_no = result.details.get('exp_no', '?')
            svd_fit = result.details.get('svd_fit', False)
            mode_str = "SVD" if svd_fit else "Global"
            node_text = f"Fit {fit_num}: {exp_no} exp ({mode_str})"
            
            fit_item = QtWidgets.QTreeWidgetItem(root_item)
            fit_item.setText(0, node_text)
            fit_item.setData(0, Qt.UserRole, {'type': 'fit_result', 'fit_category': 'global', 'fit_number': fit_num})
        
        # Restore Single Fits
        for fit_num, result in experiment.fitting.fit_records.single_fits.items():
            exp_no = result.details.get('exp_no', '?')
            node_text = f"Fit {fit_num}: {exp_no} exp (Single Trace)"
            
            fit_item = QtWidgets.QTreeWidgetItem(root_item)
            fit_item.setText(0, node_text)
            fit_item.setData(0, Qt.UserRole, {'type': 'fit_result', 'fit_category': 'single', 'fit_number': fit_num})

    def on_tree_selection_changed(self, current_item, previous_item):
        """Retrieves the experiment object from the dictionary based on the clicked item."""
        if not current_item:
            return

        parent = current_item.parent()

        if parent is None:
            exp_id = current_item.data(0, Qt.UserRole)
            target_experiment = self.experiments.get(exp_id)

            if target_experiment:
                self.mw._set_workspace_mode(show_results=False)
                self.mw.settings_manager._load_dataset_settings()
                self.mw.preprocessing_controller.update_history_list()
        else:
            node_data = current_item.data(0, Qt.UserRole)
            if isinstance(node_data, dict) and node_data.get('type') == 'fit_result':
                self.mw._set_workspace_mode(show_results=True)
                self.mw.tabMain.setCurrentWidget(self.mw.pageResults)
                fit_category = node_data.get('fit_category')

                if fit_category == 'global':
                    self.mw.stackedResultsMain.setCurrentWidget(self.mw.pageGlobalFit)
                    self.mw.plot_controller.plot_current_data_global_fit()
                elif fit_category == 'single':
                    self.mw.stackedResultsMain.setCurrentWidget(self.mw.pageSingleFit)
                    self.mw.plot_controller.plot_current_data_single_fit()

    def close_experiment_node(self, item):
        """Safely removes an entire experiment and all its settings/fits from the app."""
        reply = QtWidgets.QMessageBox.question(
            self.mw,
            'Close experiment',
            'Are you sure you want to close this experiment?\nThis will delete the entire dataset and all associated mappings from memory.',
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
            QtWidgets.QMessageBox.StandardButton.No
        )

        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            exp_id = item.data(0, Qt.UserRole)
            root = self.mw.treeExperiment.invisibleRootItem()
            root.removeChild(item)

            if exp_id in self.experiments:
                del self.experiments[exp_id]
            if exp_id in self.mw.dataset_settings:
                del self.mw.dataset_settings[exp_id]

            if self.mw.treeExperiment.topLevelItemCount() > 0:
                next_item = self.mw.treeExperiment.topLevelItem(0)
                self.mw.treeExperiment.setCurrentItem(next_item)
            else:
                empty_msg = "No experiments have been loaded.\nPlease select one from Project Explorer."
                if hasattr(self.mw, 'mplWidget'):
                    self.mw.plot_controller._clear_plot_with_message(self.mw.mplWidget, empty_msg)
                if hasattr(self.mw, 'svdMplWidget'):
                    self.mw.plot_controller._clear_plot_with_message(self.mw.svdMplWidget, empty_msg)
                if hasattr(self.mw, 'fittingPreviewMplWidget'):
                    self.mw.plot_controller._clear_plot_with_message(self.mw.fittingPreviewMplWidget, empty_msg)
                if hasattr(self.mw, 'preprocessedMplWidget'):
                    self.mw.plot_controller._clear_plot_with_message(self.mw.preprocessedMplWidget, empty_msg)
                self.mw._enable_controls(False)

            self.mw.statusBar().showMessage("The experiment has been successfully closed and memory has been freed.", 5000)

    def get_experiment(self) -> Experiment:
        """Returns the Experiment object for the currently selected tree item."""
        item = self.mw.treeExperiment.currentItem()
        if item is None:
            return None

        parent_item = item
        while parent_item.parent() is not None:
            parent_item = parent_item.parent()

        exp_id = parent_item.data(0, Qt.UserRole)
        return self.experiments.get(exp_id)
