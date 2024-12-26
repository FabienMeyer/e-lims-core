"""Device under test export module."""

from __future__ import annotations

from typing import TYPE_CHECKING

from e_lims_core.utils.dut.export.export import Export
from e_lims_core.utils.dut.tray import Tray
from e_lims_core.utils.files.file_props import FileProps, FileSuffix

if TYPE_CHECKING:
    import pandas as pd


class Export2Csv(Export):
    """Represents a class for exporting trays of devices under test (DUT) to CSV.

    Attributes
    ----------
        trays (list[Tray]): The trays to export.
        file_props (FileProps): The file properties.

    """

    def __init__(self, trays: list[Tray], file_props: FileProps) -> None:
        """Initialize the Trays2Csv object."""
        self.trays = trays
        self.file_props = file_props
        self.file_props.suffix = FileSuffix.CSV

    def generate(self) -> dict[str, pd.DataFrame]:
        """Generate CSV file/s."""
        return {tray.name: tray.get_tray() for tray in self.trays}

    def export(self) -> None:
        """Export the trays to CSV file/s."""
        data = self.generate()
        for tray_name, df_tray in data.items():
            self.file_props.name = tray_name
            df_tray.to_csv(self.file_props.file_path(), index=True)
