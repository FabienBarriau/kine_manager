"""
Built in hasher.
Warning, not safe to store passwords in a database !
"""
from kinemanager.externalities.hasher.hasher import Hasher


class BuiltinHasher(Hasher):
    """
    Built in hasher.
    """

    def hash(self, data: bytes) -> str:
        return str(hash(data))

    def verify_hash(self, to_verify: bytes, hashed: str) -> bool:
        return self.hash(to_verify) == hashed
