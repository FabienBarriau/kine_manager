"""
Test activate user.
"""
import pytest

from kinemanager.externalities.token_manager.token_manager import TokenManager
from kinemanager.models.domain import TokenData, UserRegister
from kinemanager.models.error import UserNotExists
from kinemanager.services.user_management import ActivateUser, RegisterUser


def test_user_not_exists(
    activate_user: ActivateUser,
    token_manager: TokenManager,
):
    """
    User want to activate an non existing account.
    """
    token = token_manager.encode(TokenData(username="JohnDoe"))
    with pytest.raises(UserNotExists):
        activate_user(token=token)


def test_activate_user(
    register_user: RegisterUser,
    activate_user: ActivateUser,
    token_manager: TokenManager,
):
    """
    User activate his account.
    """
    john_doe = UserRegister(
        username="JohnDoe", email="johndoe@mail.com", password="mysecurepassword"
    )
    register_user(john_doe)
    token = token_manager.encode(TokenData(username="JohnDoe"))
    activate_user(token=token)
