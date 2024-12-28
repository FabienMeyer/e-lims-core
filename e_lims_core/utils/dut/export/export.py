"""Device under test export module."""

from __future__ import annotations

from abc import ABC, abstractmethod

from e_lims_core.utils.dut.tray import Tray
from e_lims_core.utils.files.file_props import FileProps


class Export(ABC):
    """Represents abstract class for exporting devices under test (DUT).

    Attributes
    ----------
        trays (list[Tray]): The trays to export.
        file_props (FileProps): The file properties.

    """

    def __init__(self, trays: list[Tray], file_props: FileProps) -> None:
        """Initialize the TraysExport object.

        Args:
        ----
            trays (list[Tray]): The trays to export.
            file_props (FileProps): The file properties.

        """
        self.trays = trays
        self.file_props = file_props

    @abstractmethod
    def export(self) -> None:
        """Export the trays to file/s."""
