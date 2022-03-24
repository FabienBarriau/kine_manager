"""
Entities and value objects.
"""
from __future__ import annotations

from re import match
from typing import Optional, Union

from pydantic import BaseModel, validator

from kinemanager.models.error import NonValidName, NonValidPassword


class UserRegister(BaseModel):
    """
    User information for registration.
    """

    username: str
    email: str
    password: bytes

    @validator("password", pre=True)
    @classmethod
    def convert_password_from_str_to_bytes_if_needed(cls, password: Union[str, bytes]):
        """
        convertion of password.
        """
        if isinstance(password, str):
            return password.encode()
        if isinstance(password, bytes):
            return password
        raise ValueError

    @validator("username")
    @classmethod
    def check_name(cls, username: str):
        """
        Validator for username.
        """
        if bool(match(r"^[a-zA-Z \-]+$", username)):
            return username
        raise NonValidName

    @validator("password")
    @classmethod
    def check_password_format(cls, password: bytes):
        """
        Validator for password.
        """
        if len(password) < 8:
            raise NonValidPassword
        return password


class UserDatabase(BaseModel):
    """
    Stored information of an user.
    """

    uuid: str
    username: str
    encrypted_email: bytes
    hashed_password: str
    active_account: bool

    def activate(self) -> UserDatabase:
        """
        Activate the user account.
        """
        return UserDatabase(
            uuid=self.uuid,
            username=self.username,
            encrypted_email=self.encrypted_email,
            hashed_password=self.hashed_password,
            active_account=True,
        )


class UserAuthentificate(BaseModel):
    """
    User information for authentification.
    """

    username: str
    password: str


class Token(BaseModel):
    """
    Token given to the user to prove its identity.
    """

    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """
    Data encoded in a token.
    """

    username: Optional[str] = None
