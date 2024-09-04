"""Analog to digital converter tests."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Sequence

from e_lims_core.electronic_components import electronic_component


class AdcInvalidChannelError(Exception):
    """Exception raised for errors in accessing an invalid ADC channel."""

    def __init__(self, channels: int, message: str = 'ADC Channel must be between') -> None:
        """Initialize the exception."""
        self.channels = channels
        self.message = message
        super().__init__(f'{message}: 0 and {channels}')


class AdcNumberOfSamplesError(Exception):
    """Exception raised for errors in the number of samples."""

    def __init__(self, message: str = 'ADC Number of samples must be greater than 0') -> None:
        """Initialize the exception."""
        self.message = message
        super().__init__(message)


class ABCAdcChannel(ABC):
    """Abstract class for analog to digital converter channel."""

    def __init__(self, channel: int) -> None:
        """Initialize the analog to digital converter channel."""
        self._channel = channel

    @property
    def channel(self) -> int:
        """Get the channel number."""
        return self._channel

    @abstractmethod
    def voltage(self, number_of_samples: int = 1) -> float:
        """Get channel voltage."""
        ...


class ABCAdc(ABC):
    """Abstract class for analog to digital converter."""

    @abstractmethod
    def __init__(self) -> None:
        """Initialize the analog to digital converter."""
        self._type = electronic_component.ElectronicComponentTypes.ADC
        self._channels: Sequence[ABCAdcChannel] = []

    def type(self) -> electronic_component.ElectronicComponentTypes:
        """Get the electronic component type."""
        return self._type

    def channel(self, channel: int) -> ABCAdcChannel:
        """Get the ADC channel."""
        return self._channels[channel]

    @abstractmethod
    def configure(self) -> None:
        """Configure the analog to digital converter."""
        ...

    @abstractmethod
    def get_voltage(self, channel: int, number_of_samples: int = 1) -> float:
        """Get channel voltage."""
        ...
