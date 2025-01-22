"""Module used to configure the logger."""

from __future__ import annotations

from loguru import logger

from e_lims_core.utils.files.file_props import FileProps


class Logger:
    """Configures the logger for the application.

    Attributes
    ----------
        file_props (FileProps): The properties of the log file.
        level (int | str): The logging level.

    """

    def __init__(self, file_props: FileProps, level: int | str = 'DEBUG') -> None:
        """Initialize the logger.

        Args:
        ----
            file_props (FileProps): The properties of the log file.
            level (int | str): The logging level.

        """
        self.file_props = file_props
        self.level = level
        self.logger = logger

    def configure_logger(self) -> None:
        """Configure the logger."""
        log_file = self.file_props.file_path()
        self.logger.add(log_file, rotation='1 week', retention='1 month', level='DEBUG')
