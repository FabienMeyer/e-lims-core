"""Tests Tray."""

from __future__ import annotations

import re

import pandas as pd
import pytest

from e_lims_core.utils.dut.device import Device, Position
from e_lims_core.utils.dut.tray import Tray
from tests.utils.dut.conftest import INVALID_DEVICES, VALID_DEVICES_1


def test_tray_initialization(fx_tray: Tray) -> None:
    """Test the initialization of the Tray class."""
    assert fx_tray.name == 'tray_productx_1'
    assert fx_tray.number == 1
    assert fx_tray.product == 'ProductX'
    assert fx_tray.tray_size == 2
    assert fx_tray.max_column == 1
    assert fx_tray.max_row == 2


@pytest.mark.parametrize('valid_number', [1])
def test_tray_valid_number(fx_tray: Tray, valid_number: int) -> None:
    """Test the number setter of the Tray class."""
    fx_tray.number = valid_number
    assert fx_tray.number == valid_number


@pytest.mark.parametrize('invalid_number', [-1, 0])
def test_tray_invalid_number(fx_tray: Tray, invalid_number: int) -> None:
    """Test the number setter of the Tray class with a negative number."""
    with pytest.raises(ValueError, match='The tray number must be greater than 0.'):
        fx_tray.number = invalid_number


@pytest.mark.parametrize(
    'valid_product',
    [
        'ProductX',
        'ProductX1',
        'Product_X',
        'Product-X',
    ],
)
def test_tray_valid_product(fx_tray: Tray, valid_product: str) -> None:
    """Test the product setter of the Tray class with a valid product."""
    fx_tray.product = valid_product
    assert fx_tray.product == valid_product


@pytest.mark.parametrize(
    'invalid_product',
    [
        'ProductX!',
        'ProductX@',
        'ProductX#',
        'ProductX$',
    ],
)
def test_tray_invalid_product(fx_tray: Tray, invalid_product: str) -> None:
    """Test the product setter of the Tray class with an invalid product."""
    with pytest.raises(
        ValueError,
        match=f'Invalid product: {re.escape(invalid_product)}, authorized characters are alphabetic, numeric, and _-',
    ):
        fx_tray.product = invalid_product


@pytest.mark.parametrize('valid_number', [1])
def test_tray_valid_max_column(fx_tray: Tray, valid_number: int) -> None:
    """Test the max_column setter of the Tray class."""
    fx_tray.max_column = valid_number
    assert fx_tray.max_column == valid_number


@pytest.mark.parametrize('invalid_number', [-1, 0])
def test_tray_invalid_max_column(fx_tray: Tray, invalid_number: int) -> None:
    """Test the max_column setter of the Tray class with a negative number."""
    with pytest.raises(ValueError, match='The maximum number of columns must be greater than 0.'):
        fx_tray.max_column = invalid_number


@pytest.mark.parametrize('valid_number', [1])
def test_tray_valid_max_row(fx_tray: Tray, valid_number: int) -> None:
    """Test the max_row setter of the Tray class."""
    fx_tray.max_row = valid_number
    assert fx_tray.max_row == valid_number


@pytest.mark.parametrize('invalid_number', [-1, 0])
def test_tray_invalid_max_row(fx_tray: Tray, invalid_number: int) -> None:
    """Test the max_row setter of the Tray class with a negative number."""
    with pytest.raises(ValueError, match='The maximum number of rows must be greater than 0.'):
        fx_tray.max_row = invalid_number


@pytest.mark.parametrize(
    ('devices', 'expected_message'),
    [
        (VALID_DEVICES_1, None),
        (INVALID_DEVICES, 'Multiple identical name found'),
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
        (VALID_DEVICES_1, None),
        (INVALID_DEVICES, 'Multiple differential product found'),
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
        (VALID_DEVICES_1, None),
        (INVALID_DEVICES, 'Multiple identical position found'),
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


@pytest.mark.parametrize(
    ('devices', 'expected_message'),
    [
        (VALID_DEVICES_1, None),
        (INVALID_DEVICES, 'Device out of tray found'),
    ],
)
def test_check_device_position_in_tray(devices: list[Device], expected_message: str | None) -> None:
    """Test the check_device_position_in_tray method of the Tray class."""
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
            tray.check_device_position_in_tray()
    else:
        tray.check_device_position_in_tray()


def test_get_devices(fx_tray: Tray) -> None:
    """Test the get_devices method of the Tray class."""
    devices = fx_tray.get_devices()
    assert isinstance(devices, pd.DataFrame)
    assert list(devices.columns) == Device.headings()
    assert len(devices) == len(fx_tray.devices)


@pytest.mark.skip(reason='Test is working in debug mode but not in run mode')
def test_get_tray(fx_tray: Tray) -> None:
    """Test the get_tray method of the Tray class."""
    tray_df = fx_tray.get_tray()
    assert isinstance(tray_df, pd.DataFrame)
    assert tray_df.shape == (fx_tray.max_row, fx_tray.max_column)
    assert tray_df.iloc[0, 0] == 'SS1'
    assert tray_df.iloc[1, 0] == 'SS2'


@pytest.mark.parametrize(
    ('devices', 'name', 'expected_device'),
    [
        (VALID_DEVICES_1, 'SS1', VALID_DEVICES_1[0]),
        (VALID_DEVICES_1, 'SS2', VALID_DEVICES_1[1]),
        (VALID_DEVICES_1, 'NonExistent', None),
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
        (VALID_DEVICES_1, Position(column=0, row=0), VALID_DEVICES_1[0]),
        (VALID_DEVICES_1, Position(column=0, row=1), VALID_DEVICES_1[1]),
        (VALID_DEVICES_1, Position(column=1, row=1), None),
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
