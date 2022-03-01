from flask_restful import Api

from src.controllers.todo.TodoController import Todo
from src.controllers.auth.LoginController import Login

def generate_routes(app):
    api = Api(app)
    api.add_resource(Todo, "/todo")
    api.add_resource(Login, "/login")
