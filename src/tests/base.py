from flask import Flask
from flask_testing import TestCase
from server import create_app

class BaseTest(TestCase):
    TESTING = True

    def create_app(self):
        return create_app()
