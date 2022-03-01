import logging

from flask import request
from flask_restful import Resource

import src.errors.errors as error
from src.services.auth.generate_tokens import auth
from src.services.todo.get_todo_list import get_todo_list


class Todo(Resource):
    @staticmethod
    @auth.login_required
    def get():
        result = get_todo_list()
        logging.info("Successfully get todo list", dict(result=result, status_code=200))
        return result
