import requests
import json

class TodoRepository:
  source_url = "https://jsonplaceholder.typicode.com/todos?_limit=5"

  def get_todo_list(self):
    result = requests.get(self.source_url).content
    return json.loads(result)
