"""Module used to represent the properties of a file."""
from __future__ import annotations

import re
from enum import Enum
from pathlib import Path

from e_lims_core.utils.files.timestamp import TimeStamp


class FileSuffix(Enum):
    """Supported file suffixes."""

    CSV = '.csv'
    XLSX = '.xlsx'


class FileProps:
    """Represents the properties of a file.

    Attributes
    ----------
        path (Path): The directory path where the file is or will be stored.
        name (str): The name of the file, validated to contain at least six alphabetic characters.
        suffix (FileSuffix): The suffix (file extension) for the file.
        timestamp (TimeStamp | None): An optional timestamp to be appended to the file name.

    """

    def __init__(self, path: Path, name: str, suffix: FileSuffix, timestamp: TimeStamp | None = None) -> None:
        """Initialize the file properties.

        Args:
        ----
        path : Path
            The directory path for the file.
        name : str
            The name of the file, which must contain at least six alphabetic characters.
        suffix : FileSuffix
            The suffix (file extension) for the file.
        timestamp : TimeStamp, optional
            A timestamp to append to the file name. Defaults to None.

        Raises:
        ------
        ValueError
            If the file name does not meet the validation criteria.

        Notes:
        -----
        If the directory specified by `path` does not exist, it will be created with
        permissions `0o777`.

        """
        self.path = path
        self.name = name
        self.suffix = suffix
        self.timestamp = timestamp

        if not self.path.exists():
            self.path.mkdir(mode=0o777, parents=True, exist_ok=True)

    @property
    def name(self) -> str:
        """Gets the name of the file.

        Returns
        -------
            str: The name of the file.

        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """Set and validate the file name.

        Args:
        ----
        name : str
            The name of the file. Must contain at least six alphabetic characters.

        Raises:
        ------
        ValueError
            If the name does not match the validation pattern.

        """
        pattern = r'^(?=(?:[^a-zA-Z]*[a-zA-Z]){6})[a-zA-Z0-9_-]+$'
        if not bool(re.match(pattern, name)):
            msg = f'Invalid name: {name}, authorized characters are ' f'minimum 6 alphabetic, numeric, and _-'
            raise ValueError(msg)
        self._name = name

    def file_path(self) -> Path:
        """Generate the full file path, including the name, timestamp (if available), and suffix.

        Returns
        -------
        Path
            The full file path, with the name, timestamp (if available), and suffix.

        """
        if self.timestamp:
            return self.path / f'{self.name}_{self.timestamp.stamp}{self.suffix.value}'.lower()
        return self.path / f'{self.name}{self.suffix.value}'.lower()
