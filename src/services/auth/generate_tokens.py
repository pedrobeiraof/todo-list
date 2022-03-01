from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as JsonWebToken

jwt = JsonWebToken("secret key", expires_in=3600)

auth = HTTPTokenAuth("Bearer")
