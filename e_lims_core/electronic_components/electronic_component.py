"""Electronic component."""

from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Any


class ElectronicComponentTypes(Enum):
    """Electronic component types."""

    NA = auto()
    ADC = auto()
    DAC = auto()


class ElectronicComponentState(Enum):
    """Electronic component state."""

    NA = auto()
    ENABLED = auto()
    DISABLED = auto()


class ElectronicComponent:
    """Electronic component."""

    def __init__(self) -> None:
        """Initialize the electronic component."""
        self._model: str = ''
        self._symbol: str = ''
        self._type: ElectronicComponentTypes = ElectronicComponentTypes.NA

    @property
    def model(self) -> str:
        """Get the electronic component model."""
        return self._model

    @property
    def symbol(self) -> str:
        """Get the electronic component symbol."""
        return self._symbol

    @property
    def type(self) -> ElectronicComponentTypes:
        """Get the electronic component type."""
        return self._type


class ABCElectronicComponentObserver(ABC):
    """Abstract class for electronic component observer."""

    @abstractmethod
    def notify(self, subject: ABCElectronicComponentSubject) -> None:
        """Handle observer notifications."""
        ...


class ABCElectronicComponentSubject(ABC):
    """Electronic component subject."""

    @abstractmethod
    def __init__(self) -> None:
        """Initialize the electronic component observable."""
        ...

    @abstractmethod
    def subscribe(self, observer: ABCElectronicComponentObserver) -> None:
        """Subscribe to the observable."""
        ...

    @abstractmethod
    def unsubscribe(self, observer: ABCElectronicComponentObserver) -> None:
        """Unsubscribe from the observable."""
        ...

    @abstractmethod
    def notify(self, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> None:
        """Notify the observers."""
        ...


class ElectronicComponentSubject(ABCElectronicComponentSubject):
    """Electronic component subject."""

    def __init__(self) -> None:
        """Initialize the electronic component observable."""
        self._observers: list[ABCElectronicComponentObserver] = []

    def subscribe(self, observer: ABCElectronicComponentObserver) -> None:
        """Subscribe to the observable."""
        self._observers.append(observer)

    def unsubscribe(self, observer: ABCElectronicComponentObserver) -> None:
        """Unsubscribe from the observable."""
        self._observers.remove(observer)

    def notify(self, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> None:
        """Notify the observers."""
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)
