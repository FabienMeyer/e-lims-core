"""Tests Tray."""

from __future__ import annotations

import re

import pandas as pd
import pytest

from e_lims_core.utils.dut.device import Corner, Device, Position
from e_lims_core.utils.dut.tray import Tray

DEVICE_VALIDE = [
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

DEVICE_INVALIDE = [
    Device(
        number=1,
        product='ProductX',
        die='A0',
        package='R0',
        serial='SN123456',
        corner=Corner.SS,
        position=Position(column=0, row=1),
    ),
    Device(
        number=1,
        product='ProductY',
        die='A0',
        package='R0',
        serial='SN123456',
        corner=Corner.SS,
        position=Position(column=0, row=1),
    ),
]


@pytest.fixture()
def mock_tray() -> Tray:
    """Fixture for creating a mock Device instance."""
    return Tray(
        name='tray',
        number=1,
        product='ProductX',
        devices=DEVICE_VALIDE,
        max_column=1,
        max_row=2,
    )


def test_tray_initialization(mock_tray: Tray) -> None:
    """Test the initialization of the Tray class."""
    assert mock_tray.name == 'tray_productx_1'
    assert mock_tray.number == 1
    assert mock_tray.product == 'ProductX'
    assert mock_tray.tray_size == 2
    assert mock_tray.max_column == 1
    assert mock_tray.max_row == 2


@pytest.mark.parametrize('valid_number', [1])
def test_tray_valid_number(mock_tray: Tray, valid_number: int) -> None:
    """Test the number setter of the Tray class."""
    mock_tray.number = valid_number
    assert mock_tray.number == valid_number


@pytest.mark.parametrize('invalid_number', [-1, 0])
def test_tray_invalid_number(mock_tray: Tray, invalid_number: int) -> None:
    """Test the number setter of the Tray class with a negative number."""
    with pytest.raises(ValueError, match='The tray number must be greater than 0.'):
        mock_tray.number = invalid_number


@pytest.mark.parametrize(
    'valid_product',
    [
        'ProductX',
        'ProductX1',
        'Product_X',
        'Product-X',
    ],
)
def test_tray_valid_product(mock_tray: Tray, valid_product: str) -> None:
    """Test the product setter of the Tray class with a valid product."""
    mock_tray.product = valid_product
    assert mock_tray.product == valid_product


@pytest.mark.parametrize(
    'invalid_product',
    [
        'ProductX!',
        'ProductX@',
        'ProductX#',
        'ProductX$',
    ],
)
def test_tray_invalid_product(mock_tray: Tray, invalid_product: str) -> None:
    """Test the product setter of the Tray class with an invalid product."""
    with pytest.raises(
        ValueError,
        match=f'Invalid product: {re.escape(invalid_product)}, authorized characters are alphabetic, numeric, and _-',
    ):
        mock_tray.product = invalid_product


@pytest.mark.parametrize('valid_number', [1])
def test_tray_valid_max_column(mock_tray: Tray, valid_number: int) -> None:
    """Test the max_column setter of the Tray class."""
    mock_tray.max_column = valid_number
    assert mock_tray.max_column == valid_number


@pytest.mark.parametrize('invalid_number', [-1, 0])
def test_tray_invalid_max_column(mock_tray: Tray, invalid_number: int) -> None:
    """Test the max_column setter of the Tray class with a negative number."""
    with pytest.raises(ValueError, match='The maximum number of columns must be greater than 0.'):
        mock_tray.max_column = invalid_number


@pytest.mark.parametrize('valid_number', [1])
def test_tray_valid_max_row(mock_tray: Tray, valid_number: int) -> None:
    """Test the max_row setter of the Tray class."""
    mock_tray.max_row = valid_number
    assert mock_tray.max_row == valid_number


@pytest.mark.parametrize('invalid_number', [-1, 0])
def test_tray_invalid_max_row(mock_tray: Tray, invalid_number: int) -> None:
    """Test the max_row setter of the Tray class with a negative number."""
    with pytest.raises(ValueError, match='The maximum number of rows must be greater than 0.'):
        mock_tray.max_row = invalid_number


@pytest.mark.parametrize(
    ('devices', 'expected_message'),
    [
        (DEVICE_VALIDE, None),
        (DEVICE_INVALIDE, 'Multiple identical name found'),
    ],
)
def test_check_valid_device_name(devices: list[Device], expected_message: str | None) -> None:
    """Test the check_device_name method of the Tray class."""
    tray = Tray(
        name='tray',
        number=1,
        product='ProductX',
        devices=devices,
        max_column=1,
        max_row=2,
    )
    if expected_message:
        with pytest.raises(ValueError, match=expected_message):
            tray.check_device_name()
    else:
        tray.check_device_name()


@pytest.mark.parametrize(
    ('devices', 'expected_message'),
    [
        (DEVICE_VALIDE, None),
        (DEVICE_INVALIDE, 'Multiple differential product found'),
    ],
)
def test_check_device_product(devices: list[Device], expected_message: str | None) -> None:
    """Test the check_device_product method of the Tray class."""
    tray = Tray(
        name='tray',
        number=1,
        product='ProductX',
        devices=devices,
        max_column=1,
        max_row=2,
    )
    if expected_message:
        with pytest.raises(ValueError, match=expected_message):
            tray.check_device_product()
    else:
        tray.check_device_product()


@pytest.mark.parametrize(
    ('devices', 'expected_message'),
    [
        (DEVICE_VALIDE, None),
        (DEVICE_INVALIDE, 'Multiple identical position found'),
    ],
)
def test_check_device_position(devices: list[Device], expected_message: str | None) -> None:
    """Test the check_device_position method of the Tray class."""
    tray = Tray(
        name='tray',
        number=1,
        product='ProductX',
        devices=devices,
        max_column=1,
        max_row=2,
    )
    if expected_message:
        with pytest.raises(ValueError, match=expected_message):
            tray.check_device_position()
    else:
        tray.check_device_position()


def test_get_devices(mock_tray: Tray) -> None:
    """Test the get_devices method of the Tray class."""
    devices = mock_tray.get_devices()
    assert isinstance(devices, pd.DataFrame)
    assert list(devices.columns) == Device.headings()
    assert len(devices) == len(mock_tray.devices)


def test_get_tray(mock_tray: Tray) -> None:
    """Test the get_tray method of the Tray class."""
    tray_df = mock_tray.get_tray()
    assert isinstance(tray_df, pd.DataFrame)
    assert tray_df.shape == (mock_tray.max_row, mock_tray.max_column)
    assert tray_df.iloc[0, 0] == 'SS1'
    assert tray_df.iloc[1, 0] == 'SS2'

@pytest.mark.parametrize(
    ('devices', 'name', 'expected_device'),
    [
        (DEVICE_VALIDE, 'SS1', DEVICE_VALIDE[0]),
        (DEVICE_VALIDE, 'SS2', DEVICE_VALIDE[1]),
        (DEVICE_VALIDE, 'NonExistent', None),
    ],
)
def test_found_device_per_name(devices: list[Device], name: str, expected_device: Device | None) -> None:
    """Test the found_device_per_name method of the Tray class."""
    tray = Tray(
        name='tray',
        number=1,
        product='ProductX',
        devices=devices,
        max_column=1,
        max_row=2,
    )
    device = tray.found_device_per_name(name)
    assert device == expected_device


@pytest.mark.parametrize(
    ('devices', 'position', 'expected_device'),
    [
        (DEVICE_VALIDE, Position(column=0, row=0), DEVICE_VALIDE[0]),
        (DEVICE_VALIDE, Position(column=0, row=1), DEVICE_VALIDE[1]),
        (DEVICE_VALIDE, Position(column=1, row=1), None),
    ],
)
def test_found_device_per_position(devices: list[Device], position: Position, expected_device: Device | None) -> None:
    """Test the found_device_per_position method of the Tray class."""
    tray = Tray(
        name='tray',
        number=1,
        product='ProductX',
        devices=devices,
        max_column=1,
        max_row=2,
    )
    device = tray.found_device_per_position(position)
    assert device == expected_device







