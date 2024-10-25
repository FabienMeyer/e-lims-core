"""Trays."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field

import pandas as pd

from e_lims_core.utils.dut.device import Device, Position


class DevicesNameError(Exception):
    """Exception use to raise devices name error."""

    def __init__(self, devices: list[Device], *args: object) -> None:
        """Exception initialization."""
        super().__init__(*args)
        self.devices = devices

    def __str__(self) -> str:
        """Exception string representation."""
        return f'Multiple identical name found ({", ".join([device.name for device in self.devices])}).'


class DevicesProductError(Exception):
    """Exception use to raise product name error."""

    def __init__(self, devices: list[Device], *args: object) -> None:
        """Exception initialization."""
        super().__init__(*args)
        self.devices = devices

    def __str__(self) -> str:
        """Exception string representation."""
        return f'Multiple differential product found ({", ".join([device.name for device in self.devices])}).'


class DevicesPositionError(Exception):
    """Exception use to raise position name error."""

    def __init__(self, devices: list[Device], *args: object) -> None:
        """Exception initialization."""
        super().__init__(*args)
        self.devices = devices

    def __str__(self) -> str:
        """Exception string representation."""
        return f'Multiple identical position found ({", ".join([device.name for device in self.devices])}).'


class TraySizeError(Exception):
    """Exception use to raise a tray size error."""

    def __init__(self, devices: list[Device], *args: object) -> None:
        """Exception initialization."""
        super().__init__(*args)
        self.devices = devices

    def __str__(self) -> str:
        """Exception string representation."""
        return f'Tray is too small for the number of devices ({len(self.devices)}).'


@dataclass
class Tray:
    """Tray class."""

    name: str = field(init=False)
    number: int
    product: str
    devices: list[Device]
    max_column: int = 31
    max_row: int = 14
    logger: logging.Logger = logging.root

    def __post_init__(self) -> None:
        """Post initialization."""
        self.name = f'{self.name}_{self.product}_{self.number}'.lower()
        try:
            self.check_device_name()
            self.check_device_product()
            self.check_device_position()
            self.check_tray_size()
        except (DevicesNameError, DevicesProductError, DevicesPositionError, TraySizeError) as error:
            self.logger.exception('%s: %s', self.name, error.__str__())

    def file_name(self) -> str:
        """File name."""
        return f'{self.name}'

    @property
    def get_tray_size(self) -> int:
        """Get size of the tray."""
        return self.max_column * self.max_row

    def check_tray_size(self) -> None:
        """Check size of the tray."""
        if len(self.devices) > self.get_tray_size:
            raise TraySizeError(self.devices)

    def check_device_name(self) -> None:
        """Check device unique name."""
        issues = []
        for check_index, check_device in enumerate(self.devices):
            for index, device in enumerate(self.devices):
                if index != check_index and check_device.name == device.name:
                    issues.append(check_device)
        if issues:
            raise DevicesNameError(issues)

    def check_device_product(self) -> None:
        """Check device product are the same."""
        issues = []
        for check_index, check_device in enumerate(self.devices):
            for index, device in enumerate(self.devices):
                if index != check_index and check_device.product != device.product:
                    issues.append(check_device)
        if issues:
            raise DevicesNameError(issues)

    def check_device_position(self) -> None:
        """Check device unique position."""
        issues = []
        for check_index, check_device in enumerate(self.devices):
            for index, device in enumerate(self.devices):
                if index != check_index and check_device.position == device.position:
                    issues.append(check_device)
        if issues:
            raise DevicesPositionError(issues)

    def found_device_per_name(self, name: str) -> Device | None:
        """Get devices by name."""
        devices = [device for device in self.devices if device.name == name]
        return devices[0] if devices else None

    def found_device_per_position(self, position: Position) -> Device | None:
        """Get devices by position."""
        devices = [device for device in self.devices if device.position == position]
        return devices[0] if devices else None

    def get_devices(self) -> pd.DataFrame:
        """Get the devices."""
        data = [device.values() for device in self.devices]
        return pd.DataFrame(data, columns=Device.headings())

    def get_tray(self) -> pd.DataFrame:
        """Get the tray."""
        data = []
        for row in range(self.max_row):
            col_data = []
            for column in range(self.max_column):
                position = Position(column, row)
                device = self.found_device_per_position(position)
                col_data.append(device.name if device is not None else '')
            data.append(col_data)
        return pd.DataFrame(data, columns=range(self.max_column))
