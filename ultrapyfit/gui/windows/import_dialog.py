from PySide6 import QtWidgets
from PySide6.QtGui import QCloseEvent
from PySide6.QtCore import Signal
from ultrapyfit.gui.ui.ui_import_dialog import Ui_ImportDialog
from ultrapyfit.experiment import Experiment
import csv
import re
from typing import List, Tuple, Optional, Any
from dataclasses import dataclass


@dataclass
class ParsingConfig:
    """Data structure to hold current parsing configuration."""
    separator: str
    decimal: str
    is_transposed: bool  # Formerly wave_is_row
    time_col_idx: int
    wave_row_idx: int
    time_unit_str: str
    wave_unit_str: str


class ImportDialog(QtWidgets.QDialog, Ui_ImportDialog):
    """
    Dialog for importing experimental data from text/CSV files.
    Handles file previewing, separator detection, and Experiment object creation.
    """
    parameters_accepted = Signal(Experiment)

    # Pre-compiled regex for performance
    _VALUE_UNIT_PATTERN = re.compile(r'(-?\d+\.?\d*)(.*)')

    # Mapping for Separator ComboBox indices
    _SEPARATOR_MAP = {
        ';': 0, ':': 1, ',': 2, '\t': 3, '-': 4, '_': 5, ' ': 6, '|': 7
    }

    # Mapping for Unit ComboBox indices (based on original code logic)
    _WAVE_UNIT_INDICES = {'nm': 0, '\u00B5m': 1, '\u03BCm': 1, 'pm': 2}
    _TIME_UNIT_INDICES = {'ns': 0, '\u00B5s': 1, '\u03BCs': 1, 'ps': 2, 'fs': 3, 'as': 4}

    def __init__(self, parent: Optional[QtWidgets.QWidget] = None):
        super(ImportDialog, self).__init__(parent)
        self.setupUi(self)

        # Internal state
        self._file_path: str = ""
        self._cached_preview_text: str = ""  # Cache file content to avoid re-reading disk
        self._allow_close: bool = False

        self._setup_connections()
        self.FormatOptionsGroupBox.setDisabled(True)

    def _setup_connections(self):
        """Initializes all signal-slot connections."""
        self.ImportButton.clicked.connect(self.import_experiment)
        self.BrowseButton.clicked.connect(self.select_file)
        self.SepComboBox.currentIndexChanged.connect(self.toggle_custom_separator)

        # UI triggers for updating the preview table
        update_triggers = [
            self.SepComboBox.currentIndexChanged,
            self.OtherSepLineEdit.editingFinished,
            self.WaveIsRowCheckBox.stateChanged,
            self.TimeColumnSpinBox.valueChanged,
            self.WavelengthRowSpinBox.valueChanged,
            self.DecComboBox.currentIndexChanged
        ]
        for signal in update_triggers:
            signal.connect(self.update_table_preview)

    def select_file(self):
        """
        Opens a file dialog for the user to select a data file.
        If selected, attempts to auto-detect CSV dialect and loads preview.
        """
        dialog = QtWidgets.QFileDialog()
        dialog.setNameFilter("Text files (*.csv *.txt *.dat);;All files (*.*)")
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)

        if dialog.exec():
            selected_files = dialog.selectedFiles()
            if not selected_files:
                return

            self._file_path = selected_files[0]
            self.FilePathLineEdit.setText(self._file_path)
            self.FormatOptionsGroupBox.setEnabled(True)
            self.OtherSepLineEdit.setDisabled(True)

            # Read file once and cache it
            self._cached_preview_text = self._read_file(self._file_path)

            # Auto-detect format
            self._detect_dialect(self._cached_preview_text)

            # Refresh UI
            self.update_table_preview()


    def update_table_preview(self):
        """
        Main logic to parse the cached text based on UI settings
        and populate the QTableWidget.
        """
        if not self._cached_preview_text:
            return

        # config = self.get_parsing_config()

        # Parse data from the cached string, not the file

        # raw_matrix, max_cols = self._parse_text_data(
        #     self._cached_preview_text,
        #     config.separator,
        #     config.is_transposed,
        #     config.wave_row_idx,
        #     config.time_col_idx
        # )

        # if not raw_matrix or len(raw_matrix) < 2:
        #     return

        # Extract headers and data
        try:
            # Assuming row 0 is headers (wavelengths) and col 0 is index (times) after parsing logic
            # This logic assumes the structure [Header, Data...]
            preview_experiment = self.create_experiment()
            # Slice headers
            wavelength_headers = preview_experiment.wavelength
            # Slice data
            times = preview_experiment.time
            values_matrix = preview_experiment.data
            self.lblMetaShape.setText(f"{values_matrix.shape[0]} x {values_matrix.shape[1]}")

            # Auto-detect units based on headers
            cleaned_wavelengths, detected_wl_unit = self._process_wavelength_headers(wavelength_headers)
            self._auto_select_units(preview_experiment.time_unit, detected_wl_unit)

            # Update Table Widget
            self._populate_table_widget(cleaned_wavelengths, times, values_matrix)

        except Exception:
            # Handle cases where parsing creates empty or malformed lists
            pass

    def _populate_table_widget(self, headers: List[float], row_labels: List[Any], data: List[List[Any]]):
        """
        Updates the QTableWidget with processed data.

        Args:
            headers: List of float values for column headers.
            row_labels: List of values for row headers (time).
            data: 2D list of data values.
        """
        max_preview_rows = min(15, len(data))

        self.tableWidget.setRowCount(0)  # Clear
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels([f"{h:.2f}" for h in headers])
        self.tableWidget.setRowCount(max_preview_rows)
        self.tableWidget.setVerticalHeaderLabels([f"{str(t)[:6]}" for t in row_labels[:max_preview_rows]])

        for row_idx in range(max_preview_rows):
            for col_idx in range(len(headers)):
                if col_idx < len(data[row_idx]):
                    value = str(data[row_idx][col_idx])
                    item = QtWidgets.QTableWidgetItem(value)
                    self.tableWidget.setItem(row_idx, col_idx, item)

    def get_parsing_config(self) -> ParsingConfig:
        """
        Aggregates current UI state into a configuration object.

        Returns:
            ParsingConfig: The current settings from the UI.
        """

        # Helper to extract text inside parentheses: "Tab (\t)" -> "\t"
        def extract_paren(text):
            return text.split('(')[1].replace(')', '') if '(' in text else text

        decimal = extract_paren(self.DecComboBox.currentText())

        # Determine separator
        if self.OtherSepLineEdit.isEnabled():
            separator = self.OtherSepLineEdit.text()
        else:
            separator = extract_paren(self.SepComboBox.currentText())
            # Handle special display case for tab
            if separator == '\\t':
                separator = '\t'

        return ParsingConfig(
            separator=separator,
            decimal=decimal,
            is_transposed=self.WaveIsRowCheckBox.isChecked(),
            time_col_idx=int(self.TimeColumnSpinBox.value()) - 1,
            wave_row_idx=int(self.WavelengthRowSpinBox.value()) - 1,
            time_unit_str=extract_paren(self.TimeMetricComboBox.currentText()),
            wave_unit_str=extract_paren(self.WavelengthMetricComboBox.currentText())
        )

    def import_experiment(self):
        """
        Triggered by the Import button.
        Creates the Experiment object and emits it via signal.
        """
        try:
            experiment = self.create_experiment()
            self._allow_close = True
            self.parameters_accepted.emit(experiment)
            self.accept()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"The file could not be opened:\n{str(e)}")

    def closeEvent(self, event: QCloseEvent):
        """
        Intercepts the close event to ask for confirmation if not saved.
        """
        if self._allow_close:
            event.accept()
            return

        reply = QtWidgets.QMessageBox.question(
            self,
            "Confirm closing",
            "Are you sure you want to close it without importing?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
            QtWidgets.QMessageBox.StandardButton.No
        )

        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def create_experiment(self) -> Experiment:
        """
        Instantiates the Experiment object using the library's loader.

        Returns:
            Experiment: The loaded experiment object.
        """
        config = self.get_parsing_config()

        experiment = Experiment.load_data(
            self._file_path,
            config.wave_row_idx,
            config.time_col_idx,
            config.is_transposed,
            config.separator,
            config.decimal
        )

        experiment.time_unit = config.time_unit_str
        experiment.wavelength_unit = config.wave_unit_str

        # Optional logging
        # print(f"Loaded Experiment with {len(experiment.time)} time points.")
        experiment.describe_data()

        return experiment

    def toggle_custom_separator(self):
        """Enables/Disables the custom separator line edit based on combobox selection."""
        is_custom = self.SepComboBox.currentIndex() == self.SepComboBox.count() - 1
        self.OtherSepLineEdit.setEnabled(is_custom)

    # -------------------------------------------------------------------------
    # Logic / Helper Methods (Internal)
    # -------------------------------------------------------------------------

    def _auto_select_units(self, time_sample: str, wave_unit: str):
        """
        Updates the Unit ComboBoxes based on detected strings in data.

        Args:
            time_sample: A sample string from the time column (e.g., "0.01 ns").
            wave_unit: The unit detected in the wavelength header (e.g., "nm").
        """
        # Set Wavelength Unit
        if wave_unit in self._WAVE_UNIT_INDICES:
            self.WavelengthMetricComboBox.setCurrentIndex(self._WAVE_UNIT_INDICES[wave_unit])

        # Set Time Unit
        time_sample_str = str(time_sample)
        for unit, index in self._TIME_UNIT_INDICES.items():
            if unit in time_sample_str:
                self.TimeMetricComboBox.setCurrentIndex(index)
                break

    def _detect_dialect(self, sample_text: str):
        """
        Uses csv.Sniffer to guess the delimiter of the text.
        Updates the UI SepComboBox accordingly.
        """
        try:
            dialect = csv.Sniffer().sniff(sample_text)
            delimiter = dialect.delimiter

            if delimiter in self._SEPARATOR_MAP:
                self.SepComboBox.setCurrentIndex(self._SEPARATOR_MAP[delimiter])
            else:
                # Default to custom or fallback
                self.SepComboBox.setCurrentIndex(8)
        except csv.Error:
            self.SepComboBox.setCurrentIndex(8)

    def _process_wavelength_headers(self, raw_headers: List[str]) -> Tuple[List[float], str]:
        """
        Cleans header strings to extract numerical wavelength values and unit.

        Returns:
            Tuple: (List of floats, detected unit string)
        """
        clean_values = []
        detected_units = set()

        for item in raw_headers:
            val, unit = self._extract_value_and_unit(item)

            if val is not None:
                clean_values.append(val)
                if unit:
                    detected_units.add(unit)
            else:
                clean_values.append(0.0)

        final_unit = list(detected_units)[0] if detected_units else ""
        return clean_values, final_unit

    @classmethod
    def _extract_value_and_unit(cls, raw_value: Any) -> Tuple[Optional[float], str]:
        """
        Separates a string like '450 nm' into (450.0, 'nm').
        """
        text = str(raw_value).strip()
        match = cls._VALUE_UNIT_PATTERN.search(text)

        if match:
            number_str = match.group(1)
            unit_str = match.group(2).strip()
            # Clean brackets: "(nm)" -> "nm"
            unit_str = unit_str.replace('(', '').replace(')', '').strip()
            try:
                return float(number_str), unit_str
            except ValueError:
                pass

        return None, text

    @staticmethod
    def _read_file(file_path: str) -> str:
        """
        Reads the beginning of a file safely to use for previewing.

        Args:
            file_path: Path to file.
        """
        data = []
        try:
            with open(file_path, 'r', encoding='utf-8-sig', errors='replace') as f:
                for line in f:
                    if not line: break
                    data.append(line)
        except Exception as e:
            return ""
        return "".join(data)

    # @staticmethod
    # def _parse_text_data(text_data: str, separator: str, transpose: bool, skip_header_lines: int = 0,
    #                      skip_cols: int = 0) -> Tuple[List[List[str]], int]:
    #     """
    #     Parses a raw string into a matrix (list of lists) based on separator.
    #
    #     Args:
    #         text_data: The raw string content (CSV/Txt).
    #         separator: Delimiter character.
    #         transpose: Whether to swap rows and columns.
    #
    #     Returns:
    #         Tuple: (The data matrix, max number of columns found)
    #     """
    #     data = []
    #     try:
    #         lines = text_data.splitlines()
    #         reader = csv.reader(lines[skip_header_lines:], delimiter=separator)
    #         has_started_data = False
    #         for row in reader:
    #             is_empty = not row or (len(row) == 1 and not row[0].strip())
    #             if is_empty and not has_started_data:
    #                 continue
    #             if skip_cols < len(row):
    #                 cleaned_row = row[skip_cols:]
    #             else:
    #                 cleaned_row = []
    #             data.append(cleaned_row)
    #             if not is_empty:
    #                 has_started_data = True
    #     except Exception as e:
    #         return [[f"Error: {e}"]], 1
    #     if transpose and data:
    #         try:
    #             data = list(map(list, zip(*data)))
    #         except ValueError:
    #             return [], 0
    #     max_cols = max(len(row) for row in data) if data else 0
    #     return data, max_cols
