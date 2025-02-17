"""
This module sets up and runs a Flask web application, integrating with a MongoDB database to manage note-related operations.
It configures the application to use a blueprint for organizing routes and establishes a connection to the database using a specified URI.

Key Responsibilities:
- **Flask Application Initialization**: Initializes a Flask application instance, setting up the necessary configurations for running the web server.
- **MongoDB Connection**: Establishes a connection to a MongoDB database using the `MongoClient` from the `pymongo` library, and assigns the default database to the Flask app context for easy access.
- **Blueprint Registration**: Registers a blueprint (`note_bp`) that encapsulates all note-related routes, promoting modularity and separation of concerns within the application.
- **Application Execution**: Runs the Flask application in debug mode, allowing for real-time code changes and detailed error messages during development.

The module assumes that the MongoDB server is running and accessible via the provided URI, and that the `note_controller` module is correctly implemented with the necessary routes.

"""

from flask import Flask
from controllers.note_controller import note_bp
from pymongo import MongoClient
from config.config import MONGO_URI
from bson import ObjectId
import json

# Initialize the Flask application
app = Flask(__name__)

# Set up MongoDB client and database
client = MongoClient(MONGO_URI)
app.db = client.get_default_database()


# Custom JSON Encoder to handle ObjectId
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(JSONEncoder, self).default(obj)

# Use the custom JSON encoder
app.json_encoder = JSONEncoder


# Register the blueprint for note-related routes
app.register_blueprint(note_bp)

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
