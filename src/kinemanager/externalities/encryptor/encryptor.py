"""
Encryptor.
"""
from abc import ABC, abstractmethod


class Encryptor(ABC):
    """
    Encrypt and decrypt data.
    """

    @abstractmethod
    def encrypt(self, data: bytes) -> bytes:
        """Encrypt.

        Args:
            data (bytes):

        Returns:
            bytes: encryptd data.
        """

    @abstractmethod
    def decrypt(self, token: bytes) -> bytes:
        """Decrypt.

        Args:
            data (bytes):

        Returns:
            bytes: decrypted data.
        """
