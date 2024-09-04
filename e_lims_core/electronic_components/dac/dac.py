"""Digital to Analog converter."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Sequence

from e_lims_core.electronic_components import electronic_component


class DacInvalidChannelError(Exception):
    """Exception raised for errors in accessing an invalid DAC channel."""

    def __init__(self, channels: int, message: str = 'DAC Channel must be between') -> None:
        """Initialize the exception."""
        self.channels = channels
        self.message = message
        super().__init__(f'{message}: 0 and {channels}')


class DacInvalidVoltageError(Exception):
    """Exception raised for errors in setting an invalid DAC voltage."""

    def __init__(self, voltage: float, message: str = 'DAC Voltage must be between') -> None:
        """Initialize the exception."""
        self.voltage = voltage
        self.message = message
        super().__init__(f'{message}: 0 and {voltage}')


class ABCDacChannel(ABC):
    """Abstract class for digital to analog converter channel."""

    def __init__(self, channel: int) -> None:
        """Initialize the digital to analog converter channel."""
        self._channel = channel

    @property
    def channel(self) -> int:
        """Get the channel number."""
        return self._channel

    @abstractmethod
    def set_voltage(self, voltage: float) -> None:
        """Set voltage."""
        ...


class ABCDac(ABC):
    """Abstract class for digital to analog converter."""

    @abstractmethod
    def __init__(self) -> None:
        """Initialize the digital to analog converter."""
        self._type = electronic_component.ElectronicComponentTypes.DAC
        self._channels: Sequence[ABCDacChannel] = []

    def type(self) -> electronic_component.ElectronicComponentTypes:
        """Get the electronic component type."""
        return self._type

    def channel(self, channel: int) -> ABCDacChannel:
        """Get the ADC channel."""
        return self._channels[channel]

    @abstractmethod
    def configure(self) -> None:
        """Configure the digital to analog converter."""
        ...

    @abstractmethod
    def set_voltage(self, channel: int, voltage: float) -> None:
        """Set channel voltage."""
        ...
