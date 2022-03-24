"""
Publisher.
"""
from abc import ABC, abstractmethod

from kinemanager.models.domain import Token


class TokenPublisher(ABC):
    """
    Publish information.
    """

    @abstractmethod
    def __call__(self, adress: str, token: Token):
        """Send a message to an adress.

        Args:
            adress (str):
            token (Token):
        """
