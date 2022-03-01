class AuthRepository:
  default_users = [
    { "email": "user1@email.com", "password": "123456" },
    { "email": "user2@email.com", "password": "123456" },
    { "email": "user3@email.com", "password": "123456" }
  ]
  def get_user(self, email, password):
    return next((
      user for user in self.default_users
      if user["email"] == email and user["password"] == password
    ), None)
