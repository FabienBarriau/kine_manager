"""
Config getter via environement variable.
"""
import os
from typing import Any

from kinemanager.externalities.config.config import Config, ConfigParameter


class ConfigEnvVar(Config):
    """
    Get config parameter via environement variable.
    """

    def __call__(self, parameter: ConfigParameter) -> Any:
        try:
            return os.getenv(parameter)
        except:
            raise ValueError(f"{parameter} don't exists in var env")
