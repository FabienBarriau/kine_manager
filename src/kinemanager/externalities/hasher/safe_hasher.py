"""
Safe hasher.
"""
from passlib.context import CryptContext

from kinemanager.externalities.hasher.hasher import Hasher


class SafeHasher(Hasher):
    """
    Safe hasher.
    """

    def __init__(self):
        self._crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash(self, data: bytes) -> str:
        return self._crypt_context.hash(data)

    def verify_hash(self, to_verify: bytes, hashed: str) -> bool:
        return self._crypt_context.verify(to_verify, hashed)
