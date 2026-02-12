from PySide6 import QtWidgets
from PySide6.QtGui import QCloseEvent
from PySide6.QtCore import Signal
from ultrapyfit.gui.ui.ui_import_dialog import Ui_ImportDialog
from ultrapyfit.experiment import Experiment
import csv
import re


class ImportDialog(QtWidgets.QDialog, Ui_ImportDialog):
    parameters_accepted = Signal(Experiment)

    def __init__(self, parent=None):
        super(ImportDialog, self).__init__(parent)
        self.setupUi(self)
        self.file_path = ""
        self.allow_close = False
        self.ImportButton.clicked.connect(self.accept)
        self.BrowseButton.clicked.connect(self.select_file)
        self.SepComboBox.currentIndexChanged.connect(self.disable_separator_combo_box)
        self.FormatOptionsGroupBox.setDisabled(True)

        # Connect all import groupbox widgets to update the table in case of change
        self.SepComboBox.currentIndexChanged.connect(self.update_table)
        self.OtherSepLineEdit.textChanged.connect(self.update_table)
        self.WaveIsRowCheckBox.stateChanged.connect(self.update_table)
        self.TimeColumnSpinBox.valueChanged.connect(self.update_table)
        self.WavelengthRowSpinBox.valueChanged.connect(self.update_table)

    def update_table(self):
        max_row = 15
        if self.FilePathLineEdit.text() is not None:
            separator, decimal, wave_is_row, time_col, wavelength_row, time_unit, wavelength_unit = self.get_parameters()
            data, number_of_columns = self.parse_preview(self.file_path, separator, wavelength_row, time_col, wave_is_row)
            wavelengths = [column for column in data[0][1:]]
            times = [row[0] for row in data[1:]]
            matrix_data = [row[1:] for row in data[1:]]
            wavelengths_cleaned, wl_unit = self.process_wavelengths(wavelengths)
            if wl_unit == '\u00B5m' or wl_unit == '\u03BCm':
                self.WavelengthMetricComboBox.setCurrentIndex(1)
            elif wl_unit == 'pm':
                self.WavelengthMetricComboBox.setCurrentIndex(2)
            if 'ns' in data[0][0]:
                self.TimeMetricComboBox.setCurrentIndex(0)
            elif '\u00B5m' in data[0][0] or '\u03BCm' in data[0][0]:
                self.TimeMetricComboBox.setCurrentIndex(1)
            elif 'ps' in data[0][0]:
                self.TimeMetricComboBox.setCurrentIndex(2)
            elif 'fs' in data[0][0]:
                self.TimeMetricComboBox.setCurrentIndex(3)
            elif 'as' in data[0][0]:
                self.TimeMetricComboBox.setCurrentIndex(4)
            if max_row > len(matrix_data):
                max_row = len(matrix_data)
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(number_of_columns-1)
            self.tableWidget.setHorizontalHeaderLabels([f"{round(w, 2)}" for w in wavelengths_cleaned])
            self.tableWidget.setRowCount(max_row)
            for row_idx in range(max_row):
                for col_idx in range(len(wavelengths_cleaned)):
                    value = matrix_data[row_idx][col_idx]
                    item = QtWidgets.QTableWidgetItem(value)
                    self.tableWidget.setItem(row_idx, col_idx, item)
            self.tableWidget.setVerticalHeaderLabels([f"{t:.4}" for t in times])

    def closeEvent(self, event: QCloseEvent):
        """Handle when the dialog is closed via X button"""
        if self.allow_close:
            event.accept()
            return

        reply = QtWidgets.QMessageBox.question(
            self, "Bezárás megerősítése", "Biztosan be akarja zárni a mentés nélkül?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
            QtWidgets.QMessageBox.StandardButton.No
        )

        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()  # Keep the dialog open

    def accept(self):
        """Override accept to emit signal before closing"""
        try:
            experiment = self.create_experiment()
            self.parameters_accepted.emit(experiment)  # Emit the signal
            self.allow_close = True
            super().accept()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Hiba", str(e))

    def get_parameters(self):
        decimal = self.DecComboBox.currentText().split('(')[1].replace(')', '')
        wave_is_row = self.WaveIsRowCheckBox.isChecked()
        time = int(self.TimeColumnSpinBox.value()) - 1
        wavelength = int(self.WavelengthRowSpinBox.value()) - 1
        time_unit = self.TimeMetricComboBox.currentText().split('(')[1].replace(')', '')
        wavelength_unit = self.WavelengthMetricComboBox.currentText().split('(')[1].replace(')', '')
        if self.OtherSepLineEdit.isEnabled():
            separator = self.OtherSepLineEdit.text()
        else:
            separator = self.SepComboBox.currentText().split('(')[1].replace(')', '')
        return separator, decimal, wave_is_row, time, wavelength, time_unit, wavelength_unit

    def disable_separator_combo_box(self):
        if self.SepComboBox.currentIndex() == self.SepComboBox.count() - 1:
            self.OtherSepLineEdit.setEnabled(True)
        else:
            self.OtherSepLineEdit.setDisabled(True)

    def select_file(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setNameFilter("Szöveges fájlok (*.csv *.txt)")
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)
        dialog_successful = dialog.exec()
        if dialog_successful:
            self.file_path = dialog.selectedFiles()[0]
            self.FilePathLineEdit.setText(self.file_path)
            self.FormatOptionsGroupBox.setEnabled(True)
            self.OtherSepLineEdit.setDisabled(True)
            sample = self.read_file_preview(self.file_path)
            try:
                dialect = csv.Sniffer().sniff(sample)
                if dialect.delimiter == ';':
                    self.SepComboBox.setCurrentIndex(0)
                elif dialect.delimiter == ':':
                    self.SepComboBox.setCurrentIndex(1)
                elif dialect.delimiter == ',':
                    self.SepComboBox.setCurrentIndex(2)
                elif dialect.delimiter == '\t':
                    self.SepComboBox.setCurrentIndex(3)
                elif dialect.delimiter == '-':
                    self.SepComboBox.setCurrentIndex(4)
                elif dialect.delimiter == '_':
                    self.SepComboBox.setCurrentIndex(5)
                elif dialect.delimiter == ' ':
                    self.SepComboBox.setCurrentIndex(6)
                elif dialect.delimiter == '|':
                    self.SepComboBox.setCurrentIndex(7)
            except csv.Error:
                self.SepComboBox.setCurrentIndex(8)
                pass
            self.update_table()

    @staticmethod
    def read_file_preview(file_path, num_lines=15, max_bytes=16384):
        """
        Reads the first 'num_lines' of a file safely.

        Args:
            file_path (str): Path to the file.
            num_lines (int): Max lines to read (default 15).
            max_bytes (int): Safety limit to stop reading if lines are massive.

        Returns:
            str: A single string containing the preview data.
        """
        preview_data = []
        current_bytes = 0

        try:
            # 'utf-8-sig' handles standard UTF-8 AND Excel's BOM signature
            # 'errors="replace"' puts a  character instead of crashing on weird bytes
            with open(file_path, 'r', encoding='utf-8-sig', errors='replace') as f:

                for _ in range(num_lines):
                    # Read one line
                    line = f.readline()

                    # Stop if end of file
                    if not line:
                        break

                    preview_data.append(line)

                    # Safety check: Stop if we've read too much data (e.g. 16KB)
                    current_bytes += len(line.encode('utf-8'))
                    if current_bytes > max_bytes:
                        break

        except Exception as e:
            return f"Error reading file: {str(e)}"

        return "".join(preview_data)

    @staticmethod
    def parse_preview(file_path, separator, skip_rows=0, skip_cols=0, transpose=False):
        """
        Parses a file, skips rows/cols, and optionally transposes the result.

        Args:
            file_path (str): Path to file.
            separator (str): 'Tab', 'Comma', 'Semicolon', etc.
            skip_rows (int): Number of metadata lines to ignore.
            skip_cols (int): Number of columns to ignore from the left.
            transpose (bool): If True, swaps rows and columns.
        Returns:
        tuple: (data_list, max_columns)
               data_list is [[row1_col1, row1_col2], [row2_col1...]]
        """
        if separator == '\\t':
            separator = '\t'
        data = []
        try:
            with open(file_path, 'r', encoding='utf-8-sig', newline='') as f:
                for _ in range(skip_rows):
                    next(f, None)
                reader = csv.reader(f, delimiter=separator)
                for i, row in enumerate(reader):
                    if not row:
                        continue
                    if skip_cols < len(row):
                        cleaned_row = row[skip_cols:]
                    else:
                        cleaned_row = []
                    data.append(cleaned_row)
        except Exception as e:
            return [[f"Error: {e}"]], 1
        if transpose and data:
            try:
                data = list(map(list, zip(*data)))
            except ValueError:
                pass
        max_cols = max(len(row) for row in data) if data else 0

        return data, max_cols

    @staticmethod
    def clean_header_value(raw_value):
        """
        Separates a string like '450 nm' into (450.0, 'nm').
        Returns:
            tuple: (float_value, unit_string)
        """
        # Convert to string just in case
        text = str(raw_value).strip()

        # regex pattern:
        #   (-?\d+\.?\d*) -> Captures the number (integer or float, positive or negative)
        #   (.*)          -> Captures everything else (the unit)
        match = re.search(r'(-?\d+\.?\d*)(.*)', text)

        if match:
            number_str = match.group(1)
            unit_str = match.group(2).strip()

            # Clean up common brackets: "(nm)" -> "nm"
            unit_str = unit_str.replace('(', '').replace(')', '').strip()

            try:
                return float(number_str), unit_str
            except ValueError:
                pass  # Failed to convert number

        # Fallback: If no number found (e.g. just "Wavelength"), return as-is
        return None, text

    def process_wavelengths(self, raw_wavelengths):
        """
        Cleans a list of wavelength headers.
        """
        clean_values = []
        detected_units = set()

        for item in raw_wavelengths:
            val, unit = self.clean_header_value(item)

            if val is not None:
                clean_values.append(val)
                if unit:
                    detected_units.add(unit)
            else:
                # Handle error (or keep 0.0)
                clean_values.append(0.0)

        # If we found a unit (like "nm"), save it for later!
        final_unit = list(detected_units)[0] if detected_units else ""

        return clean_values, final_unit

    def create_experiment(self):
        separator, decimal, wave_is_row, time_col, wavelength_row, time_unit, wavelength_unit = self.get_parameters()
        experiment = Experiment.load_data(self.file_path, wavelength_row, time_col, wave_is_row, separator, decimal)
        experiment.time_unit = time_unit
        experiment.wavelength_unit = wavelength_unit
        print(f"Time Values: {experiment.time}")
        print(f"Wavelength Values: {experiment.wavelength}")
        print(f"Data Values: {experiment.data}")
        experiment.describe_data()
        return experiment
