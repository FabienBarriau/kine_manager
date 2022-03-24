"""
Safe encryptor.
"""
from base64 import urlsafe_b64encode

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from kinemanager.externalities.encryptor.encryptor import Encryptor


class SafeEncryptor(Encryptor):
    """
    Safe encryptor.
    """

    def __init__(self, password, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=390000,
        )
        self._fernet_encryptor = Fernet(urlsafe_b64encode(kdf.derive(password)))

    def encrypt(self, data: bytes) -> bytes:
        return self._fernet_encryptor.encrypt(data)

    def decrypt(self, token: bytes) -> bytes:
        return self._fernet_encryptor.decrypt(token)
