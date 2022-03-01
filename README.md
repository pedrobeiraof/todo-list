# TODO List

Flask api that returns 5 itens from [json placeholder todo list](https://jsonplaceholder.typicode.com/todos)

## Running

You can run the application locally with a virtual environment or using docker

### With Docker

With [docker](https://www.docker.com/) configured in your machine run the following commands

```
docker build -t todo-list:latest .
docker run -d -p 5000:5000 todo-list
```

This will start the application on port 5000

### With Virtual environment

Inside a virtual enviroment run the following

```
pip install -r requirements
python app.ts
```

This will start the application on port 5000

## Routes

After running the application, the following routes will be available on port 5000:
`POST http://localhost:5000/login`
`GET http://localhost:5000/todo`

### The login route

The login users are mocked in the code. To successfully return an access token just run the request with an **email** and **password** params.

List of available logins:
- { "email": "user1@email.com", "password": "123456" }
- { "email": "user2@email.com", "password": "123456" }
- { "email": "user3@email.com", "password": "123456" }

Exemple:
`curl -X POST 'localhost:5000/login' --data '{"email":"user1@email.com", "password":"123456"}' -H "Content-Type: application/json"`

### The todo route

Using the access-token in Authorization Header you can fetch the todo list.

Exemple:
`curl -X GET 'localhost:5000/todo' -H "Content-Type: application/json" -H "Authorization: Bearer <ACCESS_TOKEN>`
