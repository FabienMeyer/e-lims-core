"""I2C Interface."""

from __future__ import annotations

from typing import Protocol


class I2C(Protocol):
    """I2C Interface."""

    _bauderate: int

    def __init__(self) -> None:
        """Initialize the I2C interface."""

    def open(self) -> None:
        """Open the interface channel."""

    def close(self) -> None:
        """Close the interface channel."""

    @property
    def baudrate(self) -> int:
        """Get the baudrate."""
        return self._bauderate

    @baudrate.setter
    def baudrate(self, value: int) -> None:
        """Set the baudrate."""
        self._bauderate = value

    def lock(self) -> None:
        """Lock the interface."""

    def read(self) -> bytes:
        """Read data."""
        return b''

    def write(self, data: bytes) -> None:
        """Write data."""
