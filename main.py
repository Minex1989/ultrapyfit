import sys
from ultrapyfit.gui.windows.main_window import MainWindow
from PySide6 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

def trim_csv_text(
    text_data: str,
    separator: str,
    transpose: bool,
    skip_header_lines: int = 0,
    skip_cols: int = 0,
    min_data_run: int = 2
) -> List[List[str]]:
    """
    Trim metadata before/after CSV data and return cleaned rows as list of lists.

    Parameters
    - text_data: raw file contents as a single string
    - separator: field separator (e.g., ',' or ';' or '\\t')
    - transpose: if True, return transposed rows
    - skip_header_lines: additional number of lines to skip at the start of the detected data block
    - skip_cols: number of leading columns to drop from each data row
    - min_data_run: minimum contiguous lines required to consider a block as data (default 2)

    Returns
    - List of rows, each row is a list of strings (fields). Empty list if no data found.
    """
    # Normalize line endings and split
    lines = [ln.rstrip() for ln in text_data.splitlines()]
    # Remove purely empty lines but keep lines with whitespace if they might be meaningful
    nonempty_idx = [i for i, ln in enumerate(lines) if ln.strip() != ""]
    if not nonempty_idx:
        return []

    # Build candidate info: split lines and count fields
    def split_line(ln):
        # handle tab escape
        sep = '\t' if separator == '\\t' else separator
        return [f.strip() for f in ln.split(sep)]

    line_infos = []
    for i, ln in enumerate(lines):
        if ln.strip() == "":
            line_infos.append(None)
            continue
        fields = split_line(ln)
        # consider a line a candidate if at least one field contains an alphanumeric char
        has_alnum = any(re.search(r'\w', f) for f in fields)
        line_infos.append({
            "index": i,
            "raw": ln,
            "fields": fields,
            "nfields": len(fields),
            "has_alnum": has_alnum
        })

    # Collect nfields for candidate lines
    nfields_list = [info["nfields"] for info in line_infos if info and info["has_alnum"]]
    if not nfields_list:
        return []

    # Most common column count among candidate lines
    common_count = Counter(nfields_list).most_common(1)[0][0]

    # Find first contiguous run of lines with nfields == common_count and has_alnum
    start = None
    i = 0
    N = len(line_infos)
    while i < N:
        # check run starting at i
        if line_infos[i] and line_infos[i]["has_alnum"] and line_infos[i]["nfields"] == common_count:
            run_len = 1
            j = i + 1
            while j < N and line_infos[j] and line_infos[j]["has_alnum"] and line_infos[j]["nfields"] == common_count:
                run_len += 1
                j += 1
            if run_len >= min_data_run:
                start = i
                break
            i = j
        else:
            i += 1

    if start is None:
        # fallback: pick first line with common_count
        for info in line_infos:
            if info and info["has_alnum"] and info["nfields"] == common_count:
                start = info["index"]
                break
        if start is None:
            return []

    # Find last contiguous run (search backwards)
    end = None
    i = N - 1
    while i >= 0:
        if line_infos[i] and line_infos[i]["has_alnum"] and line_infos[i]["nfields"] == common_count:
            run_len = 1
            j = i - 1
            while j >= 0 and line_infos[j] and line_infos[j]["has_alnum"] and line_infos[j]["nfields"] == common_count:
                run_len += 1
                j -= 1
            if run_len >= min_data_run:
                end = i
                break
            i = j
        else:
            i -= 1

    if end is None:
        # fallback: last line with common_count
        for info in reversed(line_infos):
            if info and info["has_alnum"] and info["nfields"] == common_count:
                end = info["index"]
                break
        if end is None:
            return []

    # Apply skip_header_lines
    start += skip_header_lines
    if start > end:
        return []

    # Extract rows and drop skip_cols
    rows = []
    for idx in range(start, end + 1):
        info = line_infos[idx]
        if not info:
            continue
        fields = info["fields"]
        if skip_cols >= len(fields):
            # row becomes empty; keep as empty list
            rows.append([])
        else:
            rows.append(fields[skip_cols:])

    # Optionally transpose
    if transpose:
        # handle ragged rows by padding with empty strings
        max_cols = max((len(r) for r in rows), default=0)
        padded = [r + [""] * (max_cols - len(r)) for r in rows]
        transposed = [list(col) for col in zip(*padded)]
        return transposed

    return rows
