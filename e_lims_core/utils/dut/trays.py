"""Module used to represent a trays of devices under test (DUT)."""

from __future__ import annotations

from pathlib import Path

from e_lims_core.utils.dut.device import Corner, Device, Position
from e_lims_core.utils.dut.export.export2csv import Export2Csv
from e_lims_core.utils.dut.export.export2xlsx import Export2Excel
from e_lims_core.utils.dut.tray import Tray
from e_lims_core.utils.files.file_props import FileProps, FileSuffix


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


if __name__ == '__main__':
    devices = [
        Device(
            number=1,
            product='ProductX',
            die='A0',
            package='R0',
            serial='SN123456',
            corner=Corner.SS,
            position=Position(column=0, row=0),
        ),
        Device(
            number=2,
            product='ProductX',
            die='A0',
            package='R0',
            serial='SN123456',
            corner=Corner.SS,
            position=Position(column=2, row=1),
        ),
    ]

    tray1 = Tray(
        name='tray',
        number=1,
        product='ProductX',
        devices=devices,
        max_column=3,
        max_row=2,
    )

    tray2 = Tray(
        name='tray',
        number=2,
        product='ProductY',
        devices=devices,
        max_column=3,
        max_row=2,
    )

    file_props = FileProps(path=Path.cwd(), name='test_trays', suffix=FileSuffix.XLSX)
    trays = Trays(trays=[tray1, tray2], file_props=file_props)
    trays.export_excel()
    trays.export_csv()
