"""
Robust mail checker
"""
from validate_email import validate_email

from kinemanager.externalities.mail_checker.mail_checker import MailChecker


class RobustMailChecker(MailChecker):
    """
    Check email with the dedicated lib: validate_email.
    """

    def __call__(self, mail: str) -> bool:
        return bool(validate_email(mail))
