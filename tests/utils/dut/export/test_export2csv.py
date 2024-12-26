"""Module for testing the export to CSV functionality."""

from __future__ import annotations

from e_lims_core.utils.dut.export.export2csv import Export2Csv
from e_lims_core.utils.dut.tray import Tray
from e_lims_core.utils.files.file_props import FileProps


def test_export2csv_initialization(fx_tray: Tray, fx_csv_file_props: FileProps) -> None:
    """Test the initialization of the Export2Csv object.

    Args:
    ----
        fx_tray (Tray): Fixture for creating a Tray object.
        fx_csv_file_props (FileProps): Fixture for creating a FileProps object.

    """
    export = Export2Csv(trays=[fx_tray], file_props=fx_csv_file_props)
    assert export.trays == [fx_tray]
    assert export.file_props == fx_csv_file_props


def test_export2csv_generate(fx_tray: Tray, fx_csv_file_props: FileProps) -> None:
    """Test the generate method of the Export2Csv object.

    Args:
    ----
        fx_tray (Tray): Fixture for creating a Tray object.
        fx_csv_file_props (FileProps): Fixture for creating a FileProps object.

    """
    export = Export2Csv(trays=[fx_tray], file_props=fx_csv_file_props)
    data = export.generate()
    assert len(data) == 1
    assert fx_tray.name in data
    assert data[fx_tray.name].equals(fx_tray.get_tray())


def test_export2csv_export(fx_tray: Tray, fx_csv_file_props: FileProps) -> None:
    """Test the export method of the Export2CSV object.

    Args:
    ----
        fx_tray (Tray): Fixture for creating a Tray object.
        fx_csv_file_props (FileProps): Fixture for creating a FileProps object.

    """
    export = Export2Csv(trays=[fx_tray], file_props=fx_csv_file_props)
    export.export()
    assert (fx_csv_file_props.path / f'{fx_tray.name}.csv').exists()
