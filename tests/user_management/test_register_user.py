"""
Test register user.
"""
from uuid import UUID

import pytest

from kinemanager.externalities.data_provider.data_provider import DataProvider
from kinemanager.externalities.encryptor.encryptor import Encryptor
from kinemanager.externalities.hasher.hasher import Hasher
from kinemanager.externalities.publisher.stub_publisher import StubPublisher
from kinemanager.externalities.token_manager.token_manager import TokenManager
from kinemanager.models.domain import Token, UserRegister
from kinemanager.models.error import (
    EmailAlreadyUsed,
    NonValidEmail,
    UsernameAlreadyUsed,
)
from kinemanager.services.user_management import RegisterUser


def check_uuid_4(uuid: str) -> bool:
    """Check if input is a uuid.

    Args:
        uuid (str): An uuid.

    Returns:
        bool: True if input is a uuid.
    """
    try:
        uuid_obj = UUID(uuid, version=4)
    except ValueError:
        return False
    return str(uuid_obj) == uuid


def test_new_user_account(
    register_user: RegisterUser,
    data_provider: DataProvider,
    encryptor: Encryptor,
    hasher: Hasher,
    token_manager: TokenManager,
    publisher: StubPublisher,
):
    """
    User create a new account.
    """
    john_doe = UserRegister(
        username="JohnDoe", email="johndoe@mail.com", password="mysecurepassword"
    )
    register_user(john_doe)
    user = data_provider.get_user_in_db_by_username(username="JohnDoe")
    assert check_uuid_4(user.uuid)
    assert john_doe.username == user.username
    assert john_doe.email == encryptor.decrypt(user.encrypted_email).decode()
    assert hasher.verify_hash(john_doe.password, user.hashed_password)
    assert not user.active_account
    assert (
        token_manager.decode(publisher.adresses_messages[john_doe.email][0]).username
        == john_doe.username
    )


def test_email_already_exists_in_db(
    register_user: RegisterUser,
):
    """
    User create an account with an already existing email.
    """
    john_doe = UserRegister(
        username="JohnDoe", email="johndoe@mail.com", password="mysecurepassword"
    )
    register_user(john_doe)
    john_doe_2 = UserRegister(
        username="JohnDoe", email="johndoe@mail.com", password="mysecurepassword"
    )
    with pytest.raises(EmailAlreadyUsed):
        register_user(john_doe_2)


def test_username_already_exists_in_db(
    register_user: RegisterUser,
):
    """
    User create an account with an already existing username.
    """
    john_doe = UserRegister(
        username="JohnDoe", email="johndoe@mail.com", password="mysecurepassword"
    )
    register_user(john_doe)
    john_doe_2 = UserRegister(
        username="JohnDoe", email="john.doe@mail.com", password="mysecurepassword"
    )
    with pytest.raises(UsernameAlreadyUsed):
        register_user(john_doe_2)


def test_user_email_is_not_valid(
    register_user: RegisterUser,
):
    """
    User create an account with a non valid email.
    """
    john_doe = UserRegister(
        username="JohnDoe", email="johndoemail.com", password="mysecurepassword"
    )
    with pytest.raises(NonValidEmail):
        register_user(john_doe)
