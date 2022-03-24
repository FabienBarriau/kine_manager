"""
Hasher.
"""
from abc import ABC, abstractmethod


class Hasher(ABC):
    """
    Hasher.
    """

    @abstractmethod
    def hash(self, data: bytes) -> str:
        """Hash.

        Args:
            data (bytes):

        Returns:
            str: hashed data.
        """

    @abstractmethod
    def verify_hash(self, to_verify: bytes, hashed: str) -> bool:
        """Verify hash.

        Args:
            to_verify (bytes):
            hashed (str):

        Returns:
            bool: True if the given to_verify correspond to hashed.
        """
