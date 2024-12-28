"""Trays export CSV and Excel example."""

from pathlib import Path

from e_lims_core.utils.dut.device import Corner, Device, Position
from e_lims_core.utils.dut.tray import Tray
from e_lims_core.utils.dut.trays import Trays
from e_lims_core.utils.files.file_props import FileProps, FileSuffix


def main() -> None:
    """Trays export CSV and Excel example."""
    device1 = Device(
        number=1,
        product='PRODUCT_X',
        die='A0',
        package='R0',
        serial='SN123456',
        corner=Corner.SS,
        position=Position(column=0, row=0),
    )

    device2 = Device(
        number=2,
        product='PRODUCT_X',
        die='A0',
        package='R0',
        serial='SN123456',
        corner=Corner.SS,
        position=Position(column=0, row=1),
    )

    tray1 = Tray(
        name='tray',
        number=1,
        product='PRODUCT_X',
        devices=[device1, device2],
        max_column=2,
        max_row=2,
    )

    trays = Trays([tray1], FileProps(path=Path.cwd(), name='test_trays', suffix=FileSuffix.CSV))
    trays.export_csv()
    trays.export_excel()


if __name__ == '__main__':
    """Run main function."""
    main()
