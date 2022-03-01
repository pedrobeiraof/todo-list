from src.tests.base import BaseTest


class LoginControllerTest(BaseTest):
    def test_should_login(self):
        data = {"email": "user2@email.com", "password": "123456"}

        response = self.client.post("/login", json=data)

        assert response.status_code == 200
        assert "access_token" in response.json

    def test_should_return_error_if_invalid_params(self):
        expected_result = {"error": {"reason": "Invalid email or password."}}
        data = {"email": "test@test.com"}

        response = self.client.post("/login", json=data)

        assert response.status_code == 400 
        assert response.json == expected_result

    def test_should_return_error_if_user_does_not_exists(self):
        expected_result = {"error": {"reason": "User not found."}}

        data = {"email": "non-exist-user@test.com", "password": "any-password"}

        response = self.client.post("/login", json=data)

        assert response.status_code == 400
        assert response.json == expected_result
