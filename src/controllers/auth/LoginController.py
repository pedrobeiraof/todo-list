import logging

from flask import g, request
from flask_restful import Resource

import src.errors.errors as error
from src.services.auth.login_user import login_user
from src.services.auth.generate_tokens import auth, jwt

class Login(Resource):
    @staticmethod
    @auth.verify_token
    def verify_auth_token(token):
        g.user = None
        try:
            data = jwt.loads(token)
        except:
            return False

        if "email" in data:
            g.user = data["email"]
            return True
        return False

    @staticmethod
    def post():
        try:
            email, password = (
                request.json.get("email").strip(),
                request.json.get("password").strip(),
            )
        except Exception as why:
            logging.info("Email or password is wrong. " + str(why))
            return error.INVALID_LOGIN_PARAMS

        return login_user(email, password)
