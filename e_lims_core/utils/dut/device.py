"""Module used to represent a device under test (DUT)."""

from __future__ import annotations

import re
from dataclasses import dataclass
from enum import Enum


class Corner(Enum):
    """Corner class representing the corner type of a device under test.

    Enum values:
        * SS: Corner type SS
        * SF: Corner type SF
        * TT: Corner type TT
        * FS: Corner type FS
        * FF: Corner type FF

    """

    SS = 'SS'
    SF = 'SF'
    TT = 'TT'
    FS = 'FS'
    FF = 'FF'


@dataclass
class Position:
    """Position class representing a evice under test position in a tray.

    Attributes
    ----------
        column (int): The column index of the position.
        row (int): The row index of the position.

    """

    column: int
    row: int

    def __hash__(self) -> int:
        """Return the hash of the position.

        Returns
        -------
            int: The hash of the position.

        """
        return hash((self.row, self.column))

    def __eq__(self, other: object) -> bool:
        """Check if the position is equal to another position.

        Args:
        ----
            other (object): The object to compare with.

        Returns:
        -------
            bool: True if the positions are equal, False otherwise.

        """
        if isinstance(other, Position):
            return self.row == other.row and self.column == other.column
        return False


class Device:
    """Represents a device under test (dut).

    The device is identified by a product, die, package,
    serial number, corner, and position.

    Attributes
    ----------
        number (int): The device number.
        product (str): The product identifier.
        die (str): The die identifier.
        package (str): The package identifier.
        serial (str): The serial number of the device.
        corner (Corner): The corner type of the device.
        position (Position): The position of the device.

    """

    def __init__(
        self,
        number: int,
        product: str,
        die: str,
        package: str,
        serial: str,
        corner: Corner,
        position: Position,
    ) -> None:
        """Initialize the Device object."""
        self.number = number
        self.product = product
        self.die = die
        self.package = package
        self.serial = serial
        self.corner = corner
        self.position = position
        self.name = f'{self.corner.value}{self.number}'

    @property
    def product(self) -> str:
        """Gets the product identifier.

        Returns
        -------
            str: The product identifier.

        """
        return self._product

    @product.setter
    def product(self, product: str) -> None:
        """Set the product identifier and validate the format.

        Args:
        ----
            product (str): The product identifier.

        Raises:
        ------
            ValueError: If the product contains invalid characters.

        """
        pattern = r'^[a-zA-Z0-9_-]+$'
        if not bool(re.match(pattern, product)):
            msg = f'Invalid product: {product}, authorized characters are alphabetic, numeric, and _-'
            raise ValueError(msg)
        self._product = product

    @property
    def die(self) -> str:
        """Gets the die identifier.

        Returns
        -------
            str: The die identifier.

        """
        return self._die

    @die.setter
    def die(self, die: str) -> None:
        """Set the die identifier and validate the format.

        Args:
        ----
            die (str): The die identifier.

        Raises:
        ------
            ValueError: If the die does not follow the pattern of one alphabetic character followed by an integer.

        """
        pattern = r'^[A-Z](0|[1-9][0-9]*)$'
        if not re.match(pattern, die):
            msg = f'Invalid die: {die}, authorized one alphabetic follow by integer'
            raise ValueError(msg)
        self._die = die

    @property
    def package(self) -> str:
        """Gets the package identifier.

        Returns
        -------
            str: The package identifier.

        """
        return self._package

    @package.setter
    def package(self, package: str) -> None:
        """Set the package identifier and validate the format.

        Args:
        ----
            package (str): The package identifier.

        Raises:
        ------
            ValueError: If the package does not follow the pattern of 'R' followed by an integer.

        """
        pattern = r'^[R](0|[1-9][0-9]*)$'
        if not re.match(pattern, package):
            msg = f'Invalid package: {package}, authorized R follow by one integer'
            raise ValueError(msg)
        self._package = package

    @property
    def serial(self) -> str:
        """Gets the serial number.

        Returns
        -------
            str: The serial number.

        """
        return self._serial

    @serial.setter
    def serial(self, serial: str) -> None:
        """Set the serial number and validate the format.

        Args:
        ----
            serial (str): The serial number.

        Raises:
        ------
            ValueError: If the serial contains invalid characters.

        """
        pattern = r'^[a-zA-Z0-9]+$'
        if not bool(re.match(pattern, serial)):
            msg = f'Invalid serial: {serial}, authorized characters are alphabetic and numeric'
            raise ValueError(msg)
        self._serial = serial

    def folder(self) -> str:
        """Get the folder name for the device.

        Returns
        -------
            str: The folder name, which is the device's name.

        """
        return f'{self.name}'

    @classmethod
    def headings(cls) -> list[str]:
        """Get the headings for device information.

        Returns
        -------
            list[str]: A list of headings.

        """
        return ['name', 'product', 'die', 'package', 'serial', 'corner']

    def values(self) -> list[str]:
        """Get the values of the device attributes.

        Returns
        -------
            list[str]: A list of attribute values.

        """
        return [
            f'{self.name}',
            f'{self.product}',
            f'{self.die}',
            f'{self.package}',
            f'{self.serial}',
            f'{self.corner.value}',
        ]

    def file_name(self) -> str:
        """Get the file name for the device.

        Returns
        -------
            str: The file name, which is the device's name.

        """
        return f'{self.name}'
