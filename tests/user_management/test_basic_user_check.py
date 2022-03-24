"""
Test registration validators.
"""
import pytest

from kinemanager.models.domain import UserRegister
from kinemanager.models.error import NonValidName, NonValidPassword


def test_bad_formatted_name():
    """
    Bad formatted name.
    """
    with pytest.raises(NonValidName):
        UserRegister(
            username="JohnDoe2", email="johndoe@mail.com", password="mysecurepassword"
        )


def test_bad_formatted_password():
    """
    Bad formatted password.
    """
    with pytest.raises(NonValidPassword):
        UserRegister(username="JohnDoe", email="@johndoe@mail.com", password="123")
