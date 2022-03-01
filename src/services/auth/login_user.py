import src.errors.errors as error
from src.repositories.auth.AuthRepository import AuthRepository
from .generate_tokens import jwt

def login_user(email, password):
    if not email or not password:
        return error.INVALID_LOGIN_PARAMS

    user = AuthRepository().get_user(email, password)

    if user is None:
        return error.USER_NOT_FOUND

    access_token = jwt.dumps({"email": email})

    return { "access_token": access_token.decode() }
