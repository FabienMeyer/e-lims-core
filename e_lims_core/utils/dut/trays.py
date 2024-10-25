"""Trays."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from e_lims_core.utils.dut.device import Device, Position
    from e_lims_core.utils.dut.tray import Tray


@dataclass
class Trays:
    """Trays class."""

    trays: list[Tray]

    def found_device_per_name(self, name: str) -> list[Device | None] | None:
        """Find the device define by unique name."""
        return [tray.found_device_per_name(name) for tray in self.trays]

    def found_device_per_position(self, position: Position) -> list[Device | None] | None:
        """Find the device define by position."""
        return [tray.found_device_per_position(position) for tray in self.trays]
