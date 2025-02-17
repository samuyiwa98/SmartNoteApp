
import sys
import os
import pytest
from pymongo import MongoClient


# Add the root directory to sys.path
sys.path.insert(0, '/Users/olisamuy/Documents/CoreAi/SNotes_app/app')

from config.config import MONGO_URI
from app import app as flask_app

@pytest.fixture
def app():
    # Configure the app for testing
    flask_app.config['TESTING'] = True
    flask_app.config['MONGO_URI'] = MONGO_URI
    return flask_app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def db():
    client = MongoClient(MONGO_URI)
    db = client.get_default_database()
    yield db
    # Clean up the database after tests
    client.drop_database(db)
