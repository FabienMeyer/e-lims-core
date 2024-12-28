"""Device under test export to excel module."""

from __future__ import annotations

from openpyxl import Workbook

from e_lims_core.utils.dut.export.export import Export
from e_lims_core.utils.dut.export.tray2xlsx import Tray2Excel
from e_lims_core.utils.dut.tray import Tray
from e_lims_core.utils.files.file_props import FileProps, FileSuffix


class Export2Excel(Export):
    """Represents a class for exporting trays of devices under test (DUT) to Excel."""

    def __init__(self, trays: list[Tray], file_props: FileProps) -> None:
        """Initialize the Trays2Excel object.

        Args:
        ----
            trays (list[Tray]): List of trays to export.
            file_props (FileProps): File properties.

        """
        self.trays = trays
        self.file_props = file_props
        self.file_props.suffix = FileSuffix.XLSX

    def generate(self) -> Workbook:
        """Generate Excel file/s.

        Returns
        -------
            Workbook: Excel workbook.

        """
        workbook = Workbook()
        for tray in self.trays:
            workbook = Tray2Excel(tray, workbook).generate()
        workbook.remove(workbook['Sheet'])
        return workbook

    def export(self) -> None:
        """Export the trays to Excel file/s."""
        workbook = self.generate()
        workbook.save(self.file_props.file_path())
