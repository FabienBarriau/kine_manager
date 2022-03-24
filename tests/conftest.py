import pytest

from kinemanager.externalities.data_provider.data_provider import DataProvider
from kinemanager.externalities.data_provider.in_memory_data_provider import (
    InMemoryDataProvider,
)
from kinemanager.externalities.encryptor.dummy_encryptor import DummyEncryptor
from kinemanager.externalities.encryptor.encryptor import Encryptor
from kinemanager.externalities.hasher.builtin_hasher import BuiltinHasher
from kinemanager.externalities.hasher.hasher import Hasher
from kinemanager.externalities.mail_checker.basic_mail_checker import BasicMailChecker
from kinemanager.externalities.mail_checker.mail_checker import MailChecker
from kinemanager.externalities.publisher.publisher import TokenPublisher
from kinemanager.externalities.publisher.stub_publisher import StubPublisher
from kinemanager.externalities.token_manager.json_token_manager import BasicTokenManager
from kinemanager.externalities.token_manager.token_manager import TokenManager


@pytest.fixture
def encryptor() -> Encryptor:
    return DummyEncryptor()


@pytest.fixture
def hasher() -> Hasher:
    return BuiltinHasher()


@pytest.fixture
def token_manager() -> TokenManager:
    return BasicTokenManager()


@pytest.fixture
def data_provider() -> DataProvider:
    return InMemoryDataProvider()


@pytest.fixture
def mail_checker() -> MailChecker:
    return BasicMailChecker()


@pytest.fixture
def publisher() -> TokenPublisher:
    return StubPublisher()
