"""Module for testing the export to XLSX functionality."""

from __future__ import annotations

from openpyxl import Workbook

from e_lims_core.utils.dut.export.export2xlsx import Export2Excel
from e_lims_core.utils.dut.tray import Tray
from e_lims_core.utils.files.file_props import FileProps


def test_export2xlsx_initialization(fx_tray: Tray, fx_xlsx_file_props: FileProps) -> None:
    """Test the initialization of the Export2Csv object.

    Args:
    ----
        fx_tray (Tray): Fixture for creating a Tray object.
        fx_xlsx_file_props (FileProps): Fixture for creating a FileProps object.

    """
    export = Export2Excel(trays=[fx_tray], file_props=fx_xlsx_file_props)
    assert export.trays == [fx_tray]
    assert export.file_props == fx_xlsx_file_props


def test_export2xlsx_generate(fx_tray: Tray, fx_xlsx_file_props: FileProps) -> None:
    """Test the generate method of the Export2Csv object.

    Args:
    ----
        fx_tray (Tray): Fixture for creating a Tray object.
        fx_xlsx_file_props (FileProps): Fixture for creating a FileProps object.

    """
    export = Export2Excel(trays=[fx_tray], file_props=fx_xlsx_file_props)
    data = export.generate()
    assert isinstance(data, Workbook)
    assert len(data.sheetnames) == len(export.trays)


def test_export2xlsx_export(fx_tray: Tray, fx_xlsx_file_props: FileProps) -> None:
    """Test the export method of the Export2CSV object.

    Args:
    ----
        fx_tray (Tray): Fixture for creating a Tray object.
        fx_xlsx_file_props (FileProps): Fixture for creating a FileProps object.

    """
    export = Export2Excel(trays=[fx_tray], file_props=fx_xlsx_file_props)
    export.export()
    assert (fx_xlsx_file_props.path / f'{fx_xlsx_file_props.name}.xlsx').exists()
