"""
Basic Token.
"""
from kinemanager.externalities.token_manager.token_manager import TokenManager
from kinemanager.models.domain import Token, TokenData


class BasicTokenManager(TokenManager):
    """
    Basic Token.
    """

    def encode(self, token_data: TokenData) -> Token:
        return Token(access_token=token_data.username)

    def decode(self, token: Token) -> TokenData:
        return TokenData(username=token.access_token)
