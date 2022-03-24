"""
Basic mail checker.
"""
from re import match

from kinemanager.externalities.mail_checker.mail_checker import MailChecker


class BasicMailChecker(MailChecker):
    """
    Only check the form of the email.
    """

    def __call__(self, mail: str) -> bool:
        return bool(match(r"^.+@.+\..+$", mail))
