"""
Mail Publisher.
"""
from kinemanager.externalities.publisher.publisher import TokenPublisher
from kinemanager.models.domain import Token


class MailPublisher(TokenPublisher):
    """
    Publish message to an email.
    """

    def __call__(self, adress: str, token: Token):
        raise NotImplementedError
