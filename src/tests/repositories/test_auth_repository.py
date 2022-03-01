from src.tests.base import BaseTest
from src.repositories.auth.AuthRepository import AuthRepository


class AuthRepositoryTest(BaseTest):
    def test_should_return_user(self):
        email = "user2@email.com"
        password = "123456"

        user = AuthRepository().get_user(email, password)

        assert user == dict(email=email, password=password)

    def test_should_not_return_user(self):
        email = "fake_email_user@email.com"
        password = "123456"

        user = AuthRepository().get_user(email, password)

        assert user == None
