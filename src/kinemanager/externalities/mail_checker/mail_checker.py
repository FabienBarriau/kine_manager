"""
Mail checker.
"""
from abc import ABC, abstractmethod


class MailChecker(ABC):
    """
    Check if an email is correct.
    """

    @abstractmethod
    def __call__(self, mail: str) -> bool:
        """Verify the correctness of the email.

        Args:
            mail (str):

        Returns:
            bool: True if the mail is correct.
        """
