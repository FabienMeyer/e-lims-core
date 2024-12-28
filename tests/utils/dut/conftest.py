"""Fixture for testing the dut functionality."""

from __future__ import annotations

from pathlib import Path

import pytest

from e_lims_core.utils.dut.device import Corner, Device, Position
from e_lims_core.utils.dut.tray import Tray
from e_lims_core.utils.dut.trays import Trays
from e_lims_core.utils.files.file_props import FileProps, FileSuffix

INVALID_DEVICES = [
    Device(
        number=1,
        product='ProductX',
        die='A0',
        package='R0',
        serial='SN123456',
        corner=Corner.SS,
        position=Position(column=1, row=1),
    ),
    Device(
        number=1,
        product='ProductY',
        die='A0',
        package='R0',
        serial='SN123456',
        corner=Corner.SS,
        position=Position(column=1, row=1),
    ),
]

VALID_DEVICES_1 = [
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

VALID_DEVICES_2 = [
    Device(
        number=1,
        product='ProductY',
        die='A0',
        package='R0',
        serial='SN123456',
        corner=Corner.SS,
        position=Position(column=0, row=0),
    ),
    Device(
        number=2,
        product='ProductY',
        die='A0',
        package='R0',
        serial='SN123456',
        corner=Corner.SS,
        position=Position(column=0, row=1),
    ),
]


VALID_TRAY_1 = Tray(
    name='tray',
    number=1,
    product='ProductX',
    devices=VALID_DEVICES_1,
    max_column=1,
    max_row=2,
)


VALID_TRAY_2 = Tray(
    name='tray',
    number=1,
    product='ProductX',
    devices=VALID_DEVICES_2,
    max_column=1,
    max_row=2,
)


@pytest.fixture()
def fx_device() -> Device:
    """Fixture for creating a mock Device instance."""
    return Device(
        number=1,
        product='ProductX',
        die='A0',
        package='R0',
        serial='SN123456',
        corner=Corner.SS,
        position=Position(column=1, row=2),
    )


@pytest.fixture()
def fx_tray() -> Tray:
    """Fixture for creating a valid tray 1 instance."""
    return VALID_TRAY_1


@pytest.fixture()
def fx_trays(tmp_path: Path) -> Trays:
    """Fixture for creating a mock Trays instance."""
    file_props = FileProps(path=tmp_path, name='test_trays', suffix=FileSuffix.CSV)
    return Trays([VALID_TRAY_1, VALID_TRAY_2], file_props)
