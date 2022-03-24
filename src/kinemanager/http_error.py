from typing import Dict

from fastapi import HTTPException, status

from kinemanager.models.error import (
    EmailAlreadyUsed,
    MyAppError,
    NonValidEmail,
    NonValidName,
    NonValidPassword,
    UsernameAlreadyUsed,
    UserNotActive,
    UserNotExists,
    WrongPassword,
)

DOMAIN_ERROR_TO_HTTP_EXCEPTION: Dict[MyAppError, HTTPException] = {
    UsernameAlreadyUsed: HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Username is already used",
    ),
    EmailAlreadyUsed: HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Email is already used",
    ),
    NonValidEmail: HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Non valid email",
    ),
    NonValidPassword: HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Non valid password",
    ),
    NonValidName: HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Non valid name",
    ),
    UserNotActive: HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="User account not active",
    ),
    UserNotExists: HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="User not exist",
    ),
    WrongPassword: HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Wrong password",
    ),
}

UNKNWOWN_ERROR = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Unknwown error",
)
