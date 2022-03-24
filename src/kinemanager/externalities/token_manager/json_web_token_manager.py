"""
JWT Token.
"""
from datetime import datetime, timedelta

from jose import JWTError, jwt

from kinemanager.externalities.token_manager.token_manager import TokenManager
from kinemanager.models.domain import Token, TokenData


class JsonWebTokenManager(TokenManager):
    """
    Decode and encode JWT token.
    """

    def __init__(self, secret_key: str, expire_minutes: int = 15):
        self._secret_key = secret_key
        self._algorithm = "HS256"
        if expire_minutes is not None and expire_minutes <= 0:
            ValueError("expire_minutes must be > 0 or None")
        self._expire_delta = timedelta(minutes=expire_minutes)

    def encode(self, token_data: TokenData) -> Token:
        access_token = jwt.encode(
            token_data.dict() + {"exp": datetime.utcnow() + self._expire_delta},
            self._secret_key,
            algorithm=self._algorithm,
        )
        return Token(access_token=access_token)

    def decode(self, token: Token) -> TokenData:
        payload = jwt.decode(
            token.access_token, self._secret_key, algorithms=self._algorithm
        )
        if username := payload.get("sub") is None:
            raise JWTError("sub key is missing in jwt")
        return TokenData(username=username)
