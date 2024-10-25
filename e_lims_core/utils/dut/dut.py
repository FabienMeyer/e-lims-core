"""Provides classes and strategies for exporting trays to different formats."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Tray:
    """Represents a single tray with an ID and a name."""

    id: int
    name: str


@dataclass
class Trays:
    """Represents a collection of trays associated with a project."""

    project_id: int
    trays: list[Tray]


class ExportTrays:
    """Handles the export of trays using a specified strategy."""

    def __init__(self, trays: Trays, strategy: ExportTraysStrategy) -> None:
        """Initialize the ExportTrays with a collection of trays and an export strategy."""
        self._trays = trays
        self._strategy = strategy

    @property
    def strategy(self) -> ExportTraysStrategy:
        """Get the current export strategy."""
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: ExportTraysStrategy) -> None:
        self._strategy = strategy


class ExportTraysStrategy(ABC):
    """Abstract base class for exporting trays using different strategies."""

    @abstractmethod
    def export(self) -> None:
        """Export the given list of trays."""
        ...


class ExportTraysToExcel(ExportTraysStrategy):
    """Concrete strategy for exporting trays to an Excel file."""

    def export(self) -> None:
        """Export the given list of trays to an Excel file."""
        self.create_workbook()
        self.create_worksheet()
        self.write_data()
        self.format_data()
        self.format_print_area()
        self.save_workbook()

    def create_workbook(self) -> None:
        """Create a new workbook for exporting trays."""
        raise NotImplementedError

    def create_worksheet(self) -> None:
        """Create a new worksheet for exporting trays."""
        raise NotImplementedError

    def write_data(self) -> None:
        """Write data to the CSV file."""
        raise NotImplementedError

    def format_data(self) -> None:
        """Format the data in the worksheet."""
        raise NotImplementedError

    def format_print_area(self) -> None:
        """Format the print area in the worksheet."""
        raise NotImplementedError

    def save_workbook(self) -> None:
        """Save the workbook to a file."""
        raise NotImplementedError


class ExportTraysToCsv(ExportTraysStrategy):
    """Concrete strategy for exporting trays to a CSV file."""

    def export(self) -> None:
        """Export the given list of trays to a CSV file."""
        self.create_file()
        self.write_data()

    def create_file(self) -> None:
        """Create a new CSV file for exporting trays."""
        raise NotImplementedError

    def write_data(self) -> None:
        """Write data to the CSV file."""
        raise NotImplementedError


if __name__ == '__main__':
    trays = Trays(1, [Tray(1, 'toto'), Tray(2, 'toto'), Tray(3, 'toto')])

    export_trays = ExportTrays(trays, ExportTraysToExcel())
    export_trays.strategy.export()
    export_trays.strategy = ExportTraysToCsv()
    export_trays.strategy.export()
