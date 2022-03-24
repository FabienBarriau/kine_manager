"""
Test authentificate user.
"""
import pytest

from kinemanager.externalities.publisher.stub_publisher import StubPublisher
from kinemanager.externalities.token_manager.token_manager import TokenManager
from kinemanager.models.domain import TokenData, UserAuthentificate, UserRegister
from kinemanager.models.error import UserNotActive, UserNotExists, WrongPassword
from kinemanager.services.user_management import (
    ActivateUser,
    AuthentificateUser,
    RegisterUser,
)


def test_user_not_exists(
    authenticate_user: AuthentificateUser,
):
    """
    User want to authenticate with wrong usename.
    """
    with pytest.raises(UserNotExists):
        authenticate_user(
            UserAuthentificate(username="JohnDoe", password="mysecurepassword")
        )


def test_user_not_active(
    authenticate_user: AuthentificateUser, register_user: RegisterUser
):
    """
    User want to authenticate with a non active account.
    """
    register_user(
        UserRegister(
            username="JohnDoe", email="johndoe@mail.com", password="mysecurepassword"
        )
    )
    with pytest.raises(UserNotActive):
        authenticate_user(
            UserAuthentificate(username="JohnDoe", password="mysecurepassword")
        )


def test_user_send_wrong_password(
    authenticate_user: AuthentificateUser,
    register_user: RegisterUser,
    activate_user: ActivateUser,
    publisher: StubPublisher,
):
    """
    User want to authenticate with a wrong password.
    """
    register_user(
        UserRegister(
            username="JohnDoe", email="johndoe@mail.com", password="mysecurepassword"
        )
    )
    activate_user(token=publisher.adresses_messages["johndoe@mail.com"][0])
    with pytest.raises(WrongPassword):
        authenticate_user(
            UserAuthentificate(username="JohnDoe", password="wrongpassword")
        )


def test_user_is_authentificated(
    token_manager: TokenManager,
    authenticate_user: AuthentificateUser,
    register_user: RegisterUser,
    activate_user: ActivateUser,
    publisher: StubPublisher,
):
    """
    User authentificate
    """
    register_user(
        UserRegister(
            username="JohnDoe", email="johndoe@mail.com", password="mysecurepassword"
        )
    )
    activate_user(token=publisher.adresses_messages["johndoe@mail.com"][0])
    token = authenticate_user(
        UserAuthentificate(username="JohnDoe", password="mysecurepassword")
    )
    assert token_manager.decode(token) == TokenData(username="JohnDoe")
