import pytest

from kinemanager.externalities.data_provider.data_provider import DataProvider
from kinemanager.externalities.encryptor.encryptor import Encryptor
from kinemanager.externalities.hasher.hasher import Hasher
from kinemanager.externalities.mail_checker.mail_checker import MailChecker
from kinemanager.externalities.publisher.publisher import TokenPublisher
from kinemanager.externalities.token_manager.token_manager import TokenManager
from kinemanager.services.user_management import (
    ActivateUser,
    AuthentificateUser,
    RegisterUser,
)


@pytest.fixture
def register_user(
    data_provider: DataProvider,
    encryptor: Encryptor,
    hasher: Hasher,
    mail_checker: MailChecker,
    publisher: TokenPublisher,
    token_manager: TokenManager,
) -> RegisterUser:
    return RegisterUser(
        data_provider=data_provider,
        encryptor=encryptor,
        hasher=hasher,
        mail_checker=mail_checker,
        publisher=publisher,
        token_manager=token_manager,
    )


@pytest.fixture
def authenticate_user(
    data_provider: DataProvider, hasher: Hasher, token_manager: TokenManager
) -> AuthentificateUser:
    return AuthentificateUser(
        data_provider=data_provider, hasher=hasher, token_manager=token_manager
    )


@pytest.fixture
def activate_user(
    data_provider: DataProvider, token_manager: TokenManager
) -> ActivateUser:
    return ActivateUser(data_provider=data_provider, token_manager=token_manager)
