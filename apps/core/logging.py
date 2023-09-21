from apps.core.utils import MetaSingleton
from enum import Enum


class LevelEnum(Enum):
    info = 'INFO'
    error = 'ERROR'
    critical = 'CRITICAL'
    warning = 'WARNING'


class Logging(metaclass=MetaSingleton):
    def __init__(self, file_name: str) -> None:
        self.file_name: str = file_name

    def _write_log(self, level: LevelEnum, message: str) -> None:
        with open(self.file_name, 'a') as log_file:
            log_file.write(f"[{level.name}] {message}\n")

    def info(self, message):
        self._write_log(LevelEnum.info, message)

    def error(self, message):
        self._write_log(LevelEnum.error, message)

    def critical(self, message):
        self._write_log(LevelEnum.critical, message)

    def warning(self, message):
        self._write_log(LevelEnum.warning, message)


# class ViewExecutionTime