"""
Web API
"""
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from kinemanager.externalities.config.config import ConfigParameter
from kinemanager.externalities.config.config_env_var import ConfigEnvVar
from kinemanager.externalities.data_provider.in_memory_data_provider import (
    InMemoryDataProvider,
)
from kinemanager.externalities.encryptor.safe_encryptor import SafeEncryptor
from kinemanager.externalities.hasher.safe_hasher import SafeHasher
from kinemanager.externalities.mail_checker.robust_mail_checker import RobustMailChecker
from kinemanager.externalities.publisher.mail_publisher import MailPublisher
from kinemanager.externalities.token_manager.json_web_token_manager import (
    JsonWebTokenManager,
)
from kinemanager.http_error import DOMAIN_ERROR_TO_HTTP_EXCEPTION, UNKNWOWN_ERROR
from kinemanager.models.domain import Token, UserAuthentificate, UserRegister
from kinemanager.models.error import (
    EmailAlreadyUsed,
    NonValidEmail,
    NonValidName,
    NonValidPassword,
    UsernameAlreadyUsed,
    UserNotActive,
    UserNotExists,
    WrongPassword,
)
from kinemanager.services.user_management import (
    ActivateUser,
    AuthentificateUser,
    RegisterUser,
)

CONFIG = ConfigEnvVar()

DATA_PROVIDER = InMemoryDataProvider()
SAFE_ENCRYPTOR = SafeEncryptor(
    password=CONFIG(ConfigParameter.PASSWORD_ENCRYPTOR),
    salt=CONFIG(ConfigParameter.SALT_ENCRYPTOR),
)
SAFE_HASHER = SafeHasher()
ROBUST_MAIL_CHECKER = RobustMailChecker()
JSON_WEB_TOKEN_MANAGER = JsonWebTokenManager(
    secret_key=CONFIG(ConfigParameter.JWT_KEY),
    expire_minutes=CONFIG(ConfigParameter.TOKEN_EXPIRE_MINUTES),
)
MAIL_PUBLISHER = MailPublisher()

APP = FastAPI()


@APP.get("/user/register")
async def register_user(user_register: UserRegister):
    """
    Register user.
    """
    try:
        RegisterUser(
            data_provider=DATA_PROVIDER,
            encryptor=SAFE_ENCRYPTOR,
            hasher=SAFE_HASHER,
            mail_checker=ROBUST_MAIL_CHECKER,
            token_manager=JSON_WEB_TOKEN_MANAGER,
            publisher=MAIL_PUBLISHER,
        )(user_register)
    except NonValidEmail:
        raise DOMAIN_ERROR_TO_HTTP_EXCEPTION[NonValidEmail]
    except NonValidPassword:
        raise DOMAIN_ERROR_TO_HTTP_EXCEPTION[NonValidPassword]
    except NonValidName:
        raise DOMAIN_ERROR_TO_HTTP_EXCEPTION[NonValidName]
    except EmailAlreadyUsed:
        raise DOMAIN_ERROR_TO_HTTP_EXCEPTION[EmailAlreadyUsed]
    except UsernameAlreadyUsed:
        raise DOMAIN_ERROR_TO_HTTP_EXCEPTION[UsernameAlreadyUsed]
    except Exception:
        raise UNKNWOWN_ERROR


@APP.get("/user/activate")
async def activate_user(token: OAuth2PasswordBearer(tokenUrl="token")):
    """
    Activate user.
    """
    try:
        ActivateUser(
            data_provider=DATA_PROVIDER,
            token_manager=JSON_WEB_TOKEN_MANAGER,
        )(token)
    except UserNotExists:
        raise DOMAIN_ERROR_TO_HTTP_EXCEPTION[UserNotExists]
    except Exception:
        raise UNKNWOWN_ERROR


@APP.get("/user/authentificate", response_model=Token)
async def authentificate_user(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Authentificate user.
    """
    try:
        token = AuthentificateUser(
            data_provider=DATA_PROVIDER,
            hasher=SAFE_HASHER,
            token_manager=JSON_WEB_TOKEN_MANAGER,
        )(UserAuthentificate(username=form_data.username, password=form_data.password))
        return token
    except UserNotExists:
        raise DOMAIN_ERROR_TO_HTTP_EXCEPTION[UserNotExists]
    except WrongPassword:
        raise DOMAIN_ERROR_TO_HTTP_EXCEPTION[WrongPassword]
    except UserNotActive:
        raise DOMAIN_ERROR_TO_HTTP_EXCEPTION[UserNotActive]
    except Exception:
        raise UNKNWOWN_ERROR
