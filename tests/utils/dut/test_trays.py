"""Tests Trays."""

from e_lims_core.utils.dut.trays import Trays


def test_trays_export_csv(fx_trays: Trays) -> None:
    """Test the export_csv method of the Trays class."""
    fx_trays.export_csv()
    for tray in fx_trays.trays:
        with fx_trays.file_props.path / f'{tray.name}.csv' as f:
            assert f.read_text() == ',0\n0,SS1\n1,SS2\n'


def test_trays_export_excel(fx_trays: Trays) -> None:
    """Test the export_excel method of the Trays class."""
    fx_trays.export_excel()
