"""
User Management: register, activate, authenticate.
"""
from uuid import uuid4

from kinemanager.externalities.data_provider.data_provider import DataProvider
from kinemanager.externalities.encryptor.encryptor import Encryptor
from kinemanager.externalities.hasher.hasher import Hasher
from kinemanager.externalities.mail_checker.mail_checker import MailChecker
from kinemanager.externalities.publisher.publisher import TokenPublisher
from kinemanager.externalities.token_manager.token_manager import TokenManager
from kinemanager.models.domain import (
    Token,
    TokenData,
    UserAuthentificate,
    UserDatabase,
    UserRegister,
)
from kinemanager.models.error import (
    EmailAlreadyUsed,
    NonValidEmail,
    UsernameAlreadyUsed,
    UserNotActive,
    UserNotExists,
    WrongPassword,
)


class RegisterUser:
    """
    Register an user.
    """

    def __init__(
        self,
        data_provider: DataProvider,
        encryptor: Encryptor,
        hasher: Hasher,
        mail_checker: MailChecker,
        token_manager: TokenManager,
        publisher: TokenPublisher,
    ):
        self._data_provider = data_provider
        self._encryptor = encryptor
        self._hasher = hasher
        self._mail_checker = mail_checker
        self._token_manager = token_manager
        self._publisher = publisher

    def __call__(self, user_register: UserRegister):
        """Register an user.

        Args:
            user_register (UserRegister):

        Raises:
            NonValidEmail:
            EmailAlreadyUsed:
            UsernameAlreadyUsed:
        """
        if not self._mail_checker(user_register.email):
            raise NonValidEmail

        if self._data_provider.is_email_already_exists(
            self._encryptor.encrypt(user_register.email.encode())
        ):
            raise EmailAlreadyUsed

        if self._data_provider.is_username_already_exists(user_register.username):
            raise UsernameAlreadyUsed

        self._data_provider.write_user(
            UserDatabase(
                uuid=str(uuid4()),
                username=user_register.username,
                encrypted_email=self._encryptor.encrypt(user_register.email.encode()),
                hashed_password=self._hasher.hash(user_register.password),
                active_account=False,
            )
        )
        token = self._token_manager.encode(TokenData(username=user_register.username))
        self._publisher(adress=user_register.email, token=token)


class AuthentificateUser:
    """
    Authentificate an user.
    """

    def __init__(
        self, data_provider: DataProvider, hasher: Hasher, token_manager: TokenManager
    ):
        self._data_provider = data_provider
        self._hasher = hasher
        self._token_manager = token_manager

    def __call__(self, user_authentificate: UserAuthentificate) -> Token:
        """Authentificate an user.

        Args:
            user_authentificate (UserAuthentificate):

        Raises:
            UserNotExists:
            WrongPassword:
            UserNotActive:

        Returns:
            Token: A string that the user could utilise to prove its identity.
        """
        user_in_db = self._data_provider.get_user_in_db_by_username(
            user_authentificate.username
        )
        if user_in_db is None:
            raise UserNotExists
        if not self._hasher.verify_hash(
            user_authentificate.password.encode(), user_in_db.hashed_password
        ):
            raise WrongPassword
        if not user_in_db.active_account:
            raise UserNotActive
        return self._token_manager.encode(
            TokenData(username=user_authentificate.username)
        )


class ActivateUser:
    """
    Activate an user.
    """

    def __init__(self, data_provider: DataProvider, token_manager: TokenManager):
        self._data_provider = data_provider
        self._token_manager = token_manager

    def __call__(self, token: Token):
        """Activate an user.

        Args:
            token (Token):

        Raises:
            UserNotExists:
        """
        user_in_db = self._data_provider.get_user_in_db_by_username(
            self._token_manager.decode(token).username
        )
        if user_in_db is None:
            raise UserNotExists
        self._data_provider.write_user(user_in_db.activate())
