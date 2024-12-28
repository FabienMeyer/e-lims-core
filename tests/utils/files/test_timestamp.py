"""Tests Timestamp."""

from __future__ import annotations

from datetime import datetime, timezone

import pytest

from e_lims_core.utils.files.timestamp import TimeStamp


@pytest.fixture()
def mock_timestamp() -> datetime:
    """Fixture for a mock datetime object."""
    return datetime(2023, 10, 5, 14, 30, 45, 123456, tzinfo=timezone.utc)


def test_timestamp_initialization(mock_timestamp: datetime) -> None:
    """Test the initialization of the TimeStamp class."""
    timestamp = TimeStamp(mock_timestamp)
    assert timestamp.year == mock_timestamp.year
    assert timestamp.month == mock_timestamp.month
    assert timestamp.day == mock_timestamp.day
    assert timestamp.hour == mock_timestamp.hour
    assert timestamp.minute == mock_timestamp.minute
    assert timestamp.second == mock_timestamp.second
    assert timestamp.microsecond == mock_timestamp.microsecond


def test_timestamp_raw_time_getter(mock_timestamp: datetime) -> None:
    """Test the raw_time getter of the TimeStamp class."""
    timestamp = TimeStamp(mock_timestamp)
    assert timestamp.raw_time == mock_timestamp


def test_timestamp_raw_time_setter(mock_timestamp: datetime) -> None:
    """Test the raw_time setter of the TimeStamp class."""
    timestamp = TimeStamp(mock_timestamp)
    new_time = datetime(2022, 9, 4, 13, 20, 30, 654321, tzinfo=timezone.utc)
    timestamp.raw_time = new_time
    assert timestamp.raw_time == new_time
    assert timestamp.year == new_time.year
    assert timestamp.month == new_time.month
    assert timestamp.day == new_time.day
    assert timestamp.hour == new_time.hour
    assert timestamp.minute == new_time.minute
    assert timestamp.second == new_time.second
    assert timestamp.microsecond == new_time.microsecond


def test_timestamp_date_property(mock_timestamp: datetime) -> None:
    """Test the date property of the TimeStamp class."""
    timestamp = TimeStamp(mock_timestamp)
    assert timestamp.date == '2023_10_05'


def test_timestamp_time_property(mock_timestamp: datetime) -> None:
    """Test the time property of the TimeStamp class."""
    timestamp = TimeStamp(mock_timestamp)
    assert timestamp.time == '143045'


def test_timestamp_stamp_property(mock_timestamp: datetime) -> None:
    """Test the stamp property of the TimeStamp class."""
    timestamp = TimeStamp(mock_timestamp)
    assert timestamp.stamp == '2023_10_05_143045'


def test_timestamp_repr(mock_timestamp: datetime) -> None:
    """Test the repr method of the TimeStamp class."""
    timestamp = TimeStamp(mock_timestamp)
    assert repr(timestamp) == '2023_10_05_143045'
