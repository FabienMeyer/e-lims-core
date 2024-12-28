"""Tests Device."""

import re

import pytest

from e_lims_core.utils.dut.device import Corner, Device


def test_device_initialization(fx_device: Device) -> None:
    """Test the initialization of the Device class."""
    assert fx_device.number == 1
    assert fx_device.product == 'ProductX'
    assert fx_device.die == 'A0'
    assert fx_device.package == 'R0'
    assert fx_device.serial == 'SN123456'
    assert fx_device.corner == Corner.SS
    assert fx_device.position == fx_device.position
    assert fx_device.name == 'SS1'


@pytest.mark.parametrize(
    'valid_product',
    [
        'ProductX',
        'ProductX1',
        'Product_X',
        'Product-X',
    ],
)
def test_device_valid_product(fx_device: Device, valid_product: str) -> None:
    """Test the product setter of the Device class with a valid product."""
    fx_device.product = valid_product
    assert fx_device.product == valid_product


@pytest.mark.parametrize(
    'invalid_product',
    [
        'ProductX!',
        'ProductX@',
        'ProductX#',
        'ProductX$',
    ],
)
def test_device_invalid_product(fx_device: Device, invalid_product: str) -> None:
    """Test the product setter of the Device class with an invalid product."""
    with pytest.raises(
        ValueError,
        match=f'Invalid product: {re.escape(invalid_product)}, authorized characters are alphabetic, numeric, and _-',
    ):
        fx_device.product = invalid_product


@pytest.mark.parametrize(
    'valid_die',
    [
        'A0',
        'A1',
        'F2',
        'Z99',
    ],
)
def test_device_valid_die(fx_device: Device, valid_die: str) -> None:
    """Test the die setter of the Device class with a valid die."""
    fx_device.die = valid_die
    assert fx_device.die == valid_die


@pytest.mark.parametrize(
    'invalid_die',
    [
        'A0$',  # Contains special character
        '1A',  # Numeric character before alphabetic character
        'AA',  # No numeric character
        '11',  # No alphabetic character
        'A',  # Less than 2 characters
        'A1A',  # Alphabetic character after numeric character
        'a1',  # Lowercase alphabetic character
    ],
)
def test_device_invalid_die(fx_device: Device, invalid_die: str) -> None:
    """Test the die setter of the Device class with an invalid die."""
    with pytest.raises(
        ValueError, match=f'Invalid die: {re.escape(invalid_die)}, authorized one alphabetic follow by integer'
    ):
        fx_device.die = invalid_die


@pytest.mark.parametrize(
    'valid_package',
    [
        'R0',
        'R1',
        'R9',
    ],
)
def test_device_valid_package(fx_device: Device, valid_package: str) -> None:
    """Test the package setter of the Device class with a valid package."""
    fx_device.package = valid_package
    assert fx_device.package == valid_package


@pytest.mark.parametrize(
    'invalid_package',
    [
        'R',  # Less than 2 characters
        'R01',  # Alphabetic character after numeric character
        'R0$',  # Contains special character
        '0R0',  # Numeric character before alphabetic character
        'R0A',  # Alphabetic character after numeric character
        'A0',  # No starting R character
        'r0',  # Lowercase alphabetic character
    ],
)
def test_device_invalid_package(fx_device: Device, invalid_package: str) -> None:
    """Test the package setter of the Device class with an invalid package."""
    with pytest.raises(
        ValueError, match=f'Invalid package: {re.escape(invalid_package)}, authorized R follow by one integer'
    ):
        fx_device.package = invalid_package


@pytest.mark.parametrize(
    'valid_serial',
    [
        'SN123456',
    ],
)
def test_device_valid_serial(fx_device: Device, valid_serial: str) -> None:
    """Test the serial setter of the Device class with a valid serial."""
    fx_device.serial = valid_serial
    assert fx_device.serial == valid_serial


@pytest.mark.parametrize(
    'invalid_serial',
    [
        'ABC-123',  # Contains a hyphen
        'abc@123',  # Contains an at-sign
        '123 456',  # Contains a space
        '!',  # Contains a special character
    ],
)
def test_device_invalid_serial(fx_device: Device, invalid_serial: str) -> None:
    """Test the serial setter of the Device class with an invalid serial."""
    with pytest.raises(
        ValueError,
        match=f'Invalid serial: {re.escape(invalid_serial)}, authorized characters are alphabetic and numeric',
    ):
        fx_device.serial = invalid_serial


def test_device_folder(fx_device: Device) -> None:
    """Test the folder method of the Device class."""
    assert fx_device.folder() == 'SS1'


def test_device_headings() -> None:
    """Test the headings method of the Device class."""
    expected_headings = [
        'name',
        'product',
        'die',
        'package',
        'serial',
        'corner',
    ]
    assert Device.headings() == expected_headings


def test_device_values(fx_device: Device) -> None:
    """Test the values method of the Device class."""
    expected_values = [
        'SS1',
        'ProductX',
        'A0',
        'R0',
        'SN123456',
        'SS',
    ]
    assert fx_device.values() == expected_values


def test_device_file_name(fx_device: Device) -> None:
    """Test the file_name method of the Device class."""
    assert fx_device.file_name() == 'SS1'
