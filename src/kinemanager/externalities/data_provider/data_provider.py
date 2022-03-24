"""
Data provider.
"""
from abc import ABC, abstractmethod
from typing import Optional

from kinemanager.models.domain import UserDatabase


class DataProvider(ABC):
    """
    Data provider.
    """

    @abstractmethod
    def is_email_already_exists(self, email: bytes) -> bool:
        """Check if an encrypted email is already affilitate to an user.

        Args:
            email (bytes): An encrypted email.

        Returns:
            bool: True if the encrypted email already exists.
        """

    @abstractmethod
    def is_username_already_exists(self, username: str) -> bool:
        """Check if an username is already affilitate to an user.

        Args:
            username (str): An username.

        Returns:
            bool: True if the username aleardy exists.
        """

    @abstractmethod
    def write_user(self, user: UserDatabase):
        """Write user in the storage.

        Args:
            user (UserDatabase): An user.
        """

    @abstractmethod
    def get_user_in_db_by_username(self, username: str) -> Optional[UserDatabase]:
        """Get the user affiliate to an username.

        Args:
            username (str): An username.

        Returns:
            Optional[UserDatabase]: A user.
        """
