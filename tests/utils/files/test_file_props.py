"""Tests Files."""

from __future__ import annotations

import datetime
import pathlib

import pytest

from e_lims_core.utils.files.file_props import FileProps, FileSuffix
from e_lims_core.utils.files.timestamp import TimeStamp


@pytest.fixture()
def mock_path(tmp_path: pathlib.Path) -> pathlib.Path:
    """Fixture that creates and returns a temporary directory path."""
    path: pathlib.Path = tmp_path / 'test_dir'
    path.mkdir(parents=True, exist_ok=True)
    return path


def test_fileprops_initialization(mock_path: pathlib.Path) -> None:
    """Test the initialization of FileProps."""
    file_props = FileProps(path=mock_path, name='testfile', suffix=FileSuffix.CSV)
    assert file_props.path == mock_path
    assert file_props.name == 'testfile'
    assert file_props.suffix == FileSuffix.CSV
    assert file_props.timestamp is None


def test_fileprops_post_init_creates_directory(mock_path: pathlib.Path) -> None:
    """Test that the post-init method creates a new directory."""
    new_path = mock_path / 'new_dir'
    _ = FileProps(path=new_path, name='testfile', suffix=FileSuffix.CSV)
    assert new_path.exists()


def test_fileprops_file_path_without_timestamp(mock_path: pathlib.Path) -> None:
    """Test the file path generation without a timestamp."""
    file_props = FileProps(path=mock_path, name='testfile', suffix=FileSuffix.CSV)
    expected_path = mock_path / 'testfile.csv'
    assert file_props.file_path() == expected_path


def test_fileprops_file_path_with_timestamp(mock_path: pathlib.Path) -> None:
    """Test the file path generation with a timestamp."""
    timestamp = TimeStamp(raw_time=datetime.datetime.now(tz=datetime.timezone.utc))
    file_props = FileProps(path=mock_path, name='testfile', suffix=FileSuffix.CSV, timestamp=timestamp)
    expected_path = mock_path / f'testfile_{timestamp.stamp}.csv'
    assert file_props.file_path() == expected_path


@pytest.mark.parametrize(
    'valid_name',
    [
        'testfile',
        'TESTFILE',
        'test-file_123',
        'TEST-FILE_123',
        'Test_File_123',
    ],
)
def test_fileprops_check_name_valid(mock_path: pathlib.Path, valid_name: str) -> None:
    """Test the check_name method with a valid name."""
    file_props = FileProps(path=mock_path, name=valid_name, suffix=FileSuffix.CSV)
    try:
        file_props.name = valid_name
    except ValueError as e:
        pytest.fail(str(e))


@pytest.mark.parametrize(
    'invalid_name',
    [
        'test@file',
        'TEST FILE',
        'test',
    ],
)
@pytest.mark.xfail(raises=ValueError)
def test_fileprops_check_name_invalid_characters(mock_path: pathlib.Path, invalid_name: str) -> None:
    """Test the check_name method with various invalid names."""
    file_props = FileProps(path=mock_path, name=invalid_name, suffix=FileSuffix.CSV)
    with pytest.raises(
        ValueError,
        match=f'Invalid name: {invalid_name}, authorized characters are minmum 6 alphabetic, numeric, and _-',
    ):
        file_props.name = invalid_name
