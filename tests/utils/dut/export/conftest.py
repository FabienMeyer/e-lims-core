"""Fixture for testing the export functionality."""

from __future__ import annotations

import pathlib

import pytest
from openpyxl import Workbook

from e_lims_core.utils.dut.device import Corner, Device, Position
from e_lims_core.utils.dut.tray import Tray
from e_lims_core.utils.files.file_props import FileProps, FileSuffix


@pytest.fixture()
def fx_devices() -> list[Device]:
    """Fixture for creating a list of good devices.

    Returns
    -------
        list[Device]: List of good devices.

    """
    return [
        Device(
            number=1,
            product='ProductX',
            die='A0',
            package='R0',
            serial='SN123456',
            corner=Corner.SS,
            position=Position(column=0, row=0),
        ),
        Device(
            number=2,
            product='ProductX',
            die='A0',
            package='R0',
            serial='SN123456',
            corner=Corner.SS,
            position=Position(column=0, row=1),
        ),
    ]


@pytest.fixture()
def fx_csv_file_props(tmp_path: pathlib.Path) -> FileProps:
    """Fixture for creating FileProps object.

    Returns
    -------
        FileProps: FileProps object.

    """
    path: pathlib.Path = tmp_path / 'test_dir'
    path.mkdir(parents=True, exist_ok=True)
    return FileProps(path=path, name='testfile', suffix=FileSuffix.CSV)


@pytest.fixture()
def fx_xlsx_file_props(tmp_path: pathlib.Path) -> FileProps:
    """Fixture for creating FileProps object.

    Returns
    -------
        FileProps: FileProps object.

    """
    path: pathlib.Path = tmp_path / 'test_dir'
    path.mkdir(parents=True, exist_ok=True)
    return FileProps(path=path, name='testfile', suffix=FileSuffix.XLSX)


@pytest.fixture()
def fx_tray(fx_devices: list[Device]) -> Tray:
    """Fixture for creating Tray object.

    Returns
    -------
        Tray: Tray object.

    """
    return Tray(
        name='tray',
        number=1,
        product='ProductX',
        devices=fx_devices,
        max_column=1,
        max_row=2,
    )


@pytest.fixture()
def fx_workbook() -> Workbook:
    """Fixture for creating a workbook object.

    Returns
    -------
        Workbook: Workbook object.

    """
    return Workbook()
