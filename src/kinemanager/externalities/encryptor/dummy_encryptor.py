"""
Dummy encryptor.
Warning, this encryptor is not safe !
"""
from base64 import urlsafe_b64decode, urlsafe_b64encode

from kinemanager.externalities.encryptor.encryptor import Encryptor


class DummyEncryptor(Encryptor):
    """
    Dummy encryptor.
    """

    def encrypt(self, data: bytes) -> bytes:
        return urlsafe_b64encode(data)

    def decrypt(self, token: bytes) -> bytes:
        return urlsafe_b64decode(token)
