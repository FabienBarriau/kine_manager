"""
Stub Publisher.
"""
from typing import Dict, List

from kinemanager.externalities.publisher.publisher import TokenPublisher
from kinemanager.models.domain import Token


class StubPublisher(TokenPublisher):
    """
    Publish message to an email.
    """

    def __init__(self):
        self.adresses_messages: Dict[str, List[Token]] = {}

    def __call__(self, adress: str, token: Token):
        if adress in self.adresses_messages:
            self.adresses_messages[adress].append(token)
        else:
            self.adresses_messages[adress] = [token]
