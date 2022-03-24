"""
Config getter.
"""
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any


class ConfigParameter(str, Enum):
    """Accessible parameters in Config"""

    JWT_KEY = "JWT_KEY"
    SALT_ENCRYPTOR = "SALT_ENCRYPTOR"
    PASSWORD_ENCRYPTOR = "PASSWORD_ENCRYPTOR"
    TOKEN_EXPIRE_MINUTES = "TOKEN_EXPIRE_MINUTES"


class Config(ABC):
    """
    Get config parameter.
    """

    @abstractmethod
    def __call__(self, parameter: ConfigParameter) -> Any:
        """Get config parameter"""
