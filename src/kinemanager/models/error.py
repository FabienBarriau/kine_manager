"""
Errors
"""


class MyAppError(Exception):
    """Base class for exceptions in the app."""


class UsernameAlreadyUsed(MyAppError):
    """Exception raised when a user try to create a username with an already used username."""


class EmailAlreadyUsed(MyAppError):
    """Exception raised when a user try to create an account with an already used email."""


class NonValidEmail(MyAppError):
    """Exception raised when an email is not valid."""


class NonValidPassword(MyAppError):
    """Exception raised when a password is not enough long (8)."""


class NonValidName(MyAppError):
    """Exception raised when a name is not correct (a name is made of only letter, space and -)."""


class UserNotActive(MyAppError):
    """Exception raised when user want to authentificate but his account is not active"""


class UserNotExists(MyAppError):
    """Exception raised when a user want to authentificate but there is no account with his name"""


class WrongPassword(MyAppError):
    """Exception raised when a user want to connect but teh given password do match the true one"""
