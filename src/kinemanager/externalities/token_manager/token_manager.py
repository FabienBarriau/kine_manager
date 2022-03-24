"""
Token Manager.
"""
from abc import ABC, abstractmethod

from kinemanager.models.domain import Token, TokenData


class TokenManager(ABC):
    """
    Decode and encode token used for authentification.
    """

    @abstractmethod
    def encode(self, token_data: TokenData) -> Token:
        """Encode.

        Args:
            token_data (TokenData):

        Returns:
            Token:
        """

    @abstractmethod
    def decode(self, token: Token) -> TokenData:
        """Decode.
        Args:
            token (Token):

        Returns:
            TokenData:
        """
