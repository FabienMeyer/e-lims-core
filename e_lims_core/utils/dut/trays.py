"""Module used to represent a trays of devices under test (DUT)."""
from __future__ import annotations

from e_lims_core.utils.dut.export.export2csv import Export2Csv
from e_lims_core.utils.dut.export.export2xlsx import Export2Excel
from e_lims_core.utils.dut.tray import Tray
from e_lims_core.utils.files.file_props import FileProps


class Trays:
    """Represents a trays of devices under test (DUT).

    Attributes
    ----------
        trays (list[Tray]): The trays of devices.
        file_props (FileProps): The file properties.

    """

    def __init__(self, trays: list[Tray], file_props: FileProps) -> None:
        """Initialize the Trays object."""
        self.trays = trays
        self.file_props = file_props

    def export_csv(self) -> None:
        """Export the trays to a CSV file."""
        Export2Csv(trays=self.trays, file_props=self.file_props).export()

    def export_excel(self) -> None:
        """Export the trays to an Excel file."""
        Export2Excel(trays=self.trays, file_props=self.file_props).export()
