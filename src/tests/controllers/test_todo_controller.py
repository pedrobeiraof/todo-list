from src.tests.base import BaseTest
from src.services.auth.generate_tokens import jwt


class TodoControllerTest(BaseTest):
    def get_auth_headers(self):
      token = jwt.dumps({"email": "fake-email"}).decode("utf-8")
      return {"Authorization": "Bearer " + token}

    def test_should_return_todo_list(self):
        response = self.client.get("/todo", headers=self.get_auth_headers())

        assert response.status_code == 200

    def test_should_return_error_if_user_is_not_authorized(self):
        response = self.client.get("/todo")

        assert response.status_code == 401
        assert response.data.decode("utf-8") == "Unauthorized Access"
