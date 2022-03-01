import src.errors.errors as error
from src.repositories.todo.TodoRepository import TodoRepository

def formatter(todo_list):
    return [
        dict(id=todo.get("id"), title=todo.get("title"))
        for todo in todo_list
    ]

def get_todo_list():
    try:
        todo_list = TodoRepository().get_todo_list()
        return formatter(todo_list)
    except Exception as e:
        return error.SERVER_ERROR_500
