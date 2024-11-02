"""Module used to represent a tray of devices under test (DUT)."""

from __future__ import annotations

import re

import pandas as pd

from e_lims_core.utils.dut.device import Device, Position


class Tray:
    """Represents a tray of devices under test (DUT).

    Attributes
    ----------
        name (str): The name of the tray.
        number (int): The tray number.
        product (str): The product identifier.
        devices (list[Device]): The devices in the tray.
        max_column (int): The maximum number of columns.
        max_row (int): The maximum number of rows.

    """

    def __init__(
        self,
        name: str,
        number: int,
        product: str,
        devices: list[Device],
        max_column: int = 31,
        max_row: int = 14,
    ) -> None:
        """Initialize the Tray object."""
        self.name = f'{name}_{product}_{number}'.lower()
        self.number = number
        self.product = product
        self.devices = devices
        self.max_column = max_column
        self.max_row = max_row

    @property
    def number(self) -> int:
        """Gets the tray number.

        Returns
        -------
            int: The tray number.

        """
        return self._number

    @number.setter
    def number(self, number: int) -> None:
        """Set the tray number.

        Args:
        ----
            number (int): The tray number.

        Raises:
        ------
            ValueError: If the tray number is less than 0.

        """
        if number <= 0:
            msg = 'The tray number must be greater than 0.'
            raise ValueError(msg)
        self._number = number

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
    def max_column(self) -> int:
        """Gets the maximum number of columns.

        Returns
        -------
            int: The maximum number of columns.

        """
        return self._max_column

    @max_column.setter
    def max_column(self, max_column: int) -> None:
        """Set the maximum number of columns.

        Args:
        ----
            max_column (int): The maximum number of columns.

        Raises:
        ------
            ValueError: If the maximum number of columns is less than 1.

        """
        if max_column < 1:
            msg = 'The maximum number of columns must be greater than 0.'
            raise ValueError(msg)
        self._max_column = max_column

    @property
    def max_row(self) -> int:
        """Gets the maximum number of rows.

        Returns
        -------
            int: The maximum number of rows.

        """
        return self._max_row

    @max_row.setter
    def max_row(self, max_row: int) -> None:
        """Set the maximum number of rows.

        Args:
        ----
            max_row (int): The maximum number of rows.

        Raises:
        ------
            ValueError: If the maximum number of rows is less than 1.

        """
        if max_row < 1:
            msg = 'The maximum number of rows must be greater than 0.'
            raise ValueError(msg)
        self._max_row = max_row

    @property
    def tray_size(self) -> int:
        """Get the size of the tray.

        Returns
        -------
            int: The size of the tray.

        """
        return self.max_column * self.max_row

    def file_name(self) -> str:
        """File name for the tray.

        Returns
        -------
            str: The file name for the tray.

        """
        return f'{self.name}_{self.product}_{self.number}'

    def check_tray_size(self) -> None:
        """Check size of the tray.

        Raises
        ------
            ValueError: If the tray size is too small for the number of devices.

        """
        if len(self.devices) > self.tray_size:
            msg = f'Tray is too small for the number of devices ({len(self.devices)}).'
            raise ValueError(msg)

    def check_device_name(self) -> None:
        """Check device unique name.

        Raises
        ------
            ValueError: If the device name is not unique.

        """
        issues = []
        for check_index, check_device in enumerate(self.devices):
            for index, device in enumerate(self.devices):
                if index != check_index and check_device.name == device.name:
                    issues.append(check_device)
        if issues:
            msg = f'Multiple identical name found ({", ".join([device.name for device in issues])}).'
            raise ValueError(msg)

    def check_device_product(self) -> None:
        """Check device product are the same.

        Raises
        ------
            ValueError: If the device product are not the same.

        """
        issues = []
        for check_index, check_device in enumerate(self.devices):
            for index, device in enumerate(self.devices):
                if index != check_index and check_device.product != device.product and device.product != self.product:
                    issues.append(check_device)
        if issues:
            msg = f'Multiple differential product found ({", ".join([device.name for device in issues])}).'
            raise ValueError(msg)

    def check_device_position(self) -> None:
        """Check device unique position.

        Raises
        ------
            ValueError: If the device position is not unique.

        """
        issues = []
        for check_index, check_device in enumerate(self.devices):
            for index, device in enumerate(self.devices):
                if index != check_index and check_device.position == device.position:
                    issues.append(check_device)
        if issues:
            msg = f'Multiple identical position found ({", ".join([device.name for device in self.devices])}).'
            raise ValueError(msg)

    def get_devices(self) -> pd.DataFrame:
        """Get the devices.

        Returns
        -------
            pd.DataFrame: The devices

        """
        data = [device.values() for device in self.devices]
        return pd.DataFrame(data, columns=Device.headings())

    def get_tray(self) -> pd.DataFrame:
        """Get the tray.

        Returns
        -------
            pd.DataFrame: The tray

        """
        data = []
        for row in range(self.max_row):
            col_data = []
            for column in range(self.max_column):
                position = Position(column, row)
                device = self.found_device_per_position(position)
                col_data.append(device.name if device is not None else '')
            data.append(col_data)
        return pd.DataFrame(data, columns=range(self.max_column))

    def found_device_per_name(self, name: str) -> Device | None:
        """Get devices by name.

        Args:
        ----
            name (str): The name of the device.

        Returns:
        -------
            Device: The device with the name.

        """
        devices = [device for device in self.devices if device.name == name]
        return devices[0] if devices else None

    def found_device_per_position(self, position: Position) -> Device | None:
        """Get devices by position.

        Args:
        ----
            position (Position): The position of the device.

        Returns:
        -------
            Device: The device with the position.

        """
        devices = [device for device in self.devices if device.position == position]
        return devices[0] if devices else None
