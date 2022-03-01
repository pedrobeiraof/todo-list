from flask import Flask
from flask_testing import TestCase
from app import create_app

class BaseTest(TestCase):
    TESTING = True

    def create_app(self):
        return create_app()
