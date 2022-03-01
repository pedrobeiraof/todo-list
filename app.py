import os

from flask import Flask

from src.config import PORT, DEBUG
from src.routes import generate_routes

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True

    generate_routes(app)
    return app

if __name__ == '__main__':
    app = create_app()

    app.run(port=PORT, debug=DEBUG, use_reloader=True)