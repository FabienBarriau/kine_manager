"""
In memory data provider.
"""
from typing import Dict, Optional

from kinemanager.externalities.data_provider.data_provider import DataProvider
from kinemanager.models.domain import UserDatabase


class InMemoryDataProvider(DataProvider):
    """
    In memory data provider.
    """

    def __init__(self):
        self._users: Dict[str, UserDatabase] = {}

    def is_email_already_exists(self, email: bytes) -> bool:
        return any(user.encrypted_email == email for _, user in self._users.items())

    def is_username_already_exists(self, username: str) -> bool:
        return any(user.username == username for _, user in self._users.items())

    def write_user(self, user: UserDatabase):
        self._users[user.username] = user

    def get_user_in_db_by_username(self, username: str) -> Optional[UserDatabase]:
        return self._users.get(username, None)
