"""Timestamp."""

from __future__ import annotations

from datetime import datetime


class TimeStamp:
    """Represents a timestamp with date and time components extracted from a datetime object.

    Attributes
    ----------
    raw_time (datetime): The original datetime object.
        year (int): The year component extracted from `raw_time`.
        month (int): The month component extracted from `raw_time`.
        day (int): The day component extracted from `raw_time`.
        hour (int): The hour component extracted from `raw_time`.
        minute (int): The minute component extracted from `raw_time`.
        second (int): The second component extracted from `raw_time`.
        microsecond (int): The microsecond component extracted from `raw_time`.

    """

    def __init__(self, raw_time: datetime) -> None:
        """Initialize TimeStamp with a datetime object and extract date and time components.

        Args:
        ----
            raw_time (datetime): The original datetime to be stored and
            processed.

        """
        self.raw_time = raw_time

    @property
    def raw_time(self) -> datetime:
        """datetime: Gets the raw datetime object."""
        return self._raw_time

    @raw_time.setter
    def raw_time(self, raw_time: datetime) -> None:
        """Set the raw datetime and extract date and time components.

        Args:
        ----
        raw_time : datetime
            The datetime to be stored and processed.

        """
        self._raw_time = raw_time
        self.year = raw_time.year
        self.month = raw_time.month
        self.day = raw_time.day
        self.hour = raw_time.hour
        self.minute = raw_time.minute
        self.second = raw_time.second
        self.microsecond = raw_time.microsecond

    @property
    def date(self) -> str:
        """Gets date as a string in 'YYYY_MM_DD' format.

        Returns
        -------
            str: The date as a string in 'YYYY_MM_DD' format.

        """
        return f'{self.year}_{self.month:02}_{self.day:02}'

    @property
    def time(self) -> str:
        """Gets time as a string in 'HHMMSS' format.

        Returns
        -------
            str: The time as a string in 'HHMMSS' format.

        """
        return f'{self.hour:02}{self.minute:02}{self.second:02}'

    @property
    def stamp(self) -> str:
        """Gets the timestamp as a string in 'YYYY_MM_DD_HHMMSS' format.

        Returns
        -------
            str: The timestamp as a string in 'YYYY_MM_DD_HHMMSS' format.

        """
        return f'{self.date}_{self.time}'

    def __repr__(self) -> str:
        """Get the string representation of the timestamp.

        Returns
        -------
            str: The timestamp as a string in 'YYYY_MM_DD_HHMMSS' format.

        """
        return self.stamp
