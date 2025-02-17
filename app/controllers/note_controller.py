
"""
The note_controller module is responsible for handling HTTP requests related to note operations in the application.
It defines a set of RESTful API endpoints for creating, retrieving, updating, and deleting notes, as well as searching for notes based on keywords.
This module uses Flask's Blueprint to organize routes related to note management, promoting modularity and separation of concerns.

Key Responsibilities:
- **Add Note**: Provides an endpoint to create a new note with a title, content, and category. It returns the ID of the newly created note.
- **Get All Notes**: Offers an endpoint to retrieve all existing notes, returning them in JSON format.
- **Update Note**: Allows updating an existing note's title, content, and category by its ID. It returns the count of modified documents.
- **Delete Note**: Facilitates the deletion of a note by its ID, returning the count of deleted documents.
- **Search Notes**: Enables searching for notes based on a keyword, returning a list of matching notes.

The module interacts with the service layer to perform CRUD operations and utilizes utility functions for additional features like category suggestion.
Error handling is implemented to manage invalid input formats, ensuring robust API behavior.
"""

from flask import Blueprint, request, jsonify
from bson import ObjectId
from service.note_service import create_note, list_notes, modify_note, remove_note, find_notes
from utils.categorisation import suggest_category

# Create a Blueprint for the notes, which allows us to organize the routes related to notes
note_bp = Blueprint('note_bp', __name__)

@note_bp.route('/notes', methods=['POST'])
def add_note():
    data = request.json # Parse the incoming JSON request data
    result = create_note(data['title'], data['content'], data['category'])  # Parse the incoming JSON request data
    return jsonify({"inserted_id": str(result.inserted_id)}), 201 # Return the ID of the created note with HTTP 201 status

@note_bp.route('/notes/all', methods=['GET'])
def get_notes():
    notes = list_notes()
    return jsonify(notes), 200

@note_bp.route('/notes/<note_id>', methods=['GET'])
def get_notes_by_id(note_id):
    try:
        # Convert the note_id to ObjectId
        note_id = ObjectId(note_id)
    except Exception as e:
        return jsonify({"error": "Invalid note ID format"}), 400
    note = get_notes_by_id()
    return jsonify(note), 200

@note_bp.route('/notes/update/<note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.json
    try:
        # Convert the note_id to ObjectId
        note_id = ObjectId(note_id)
    except Exception as e:
        return jsonify({"error": "Invalid note ID format"}), 400

    result = modify_note(note_id, data['title'], data['content'], data['category'])
    return jsonify({"modified_count": result.modified_count}), 200 # Return the number of modified documents with HTTP 200 status

@note_bp.route('/notes/remove/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    try:
        # Convert the note_id to ObjectId
        note_id = ObjectId(note_id)
    except Exception as e:
        return jsonify({"error": "Invalid note ID format"}), 400
    result = remove_note(note_id)
    return jsonify({"deleted_count": result.deleted_count}), 200 # Return the number of deleted documents with HTTP 200 status

@note_bp.route('/notes/search', methods=['GET'])
def search_notes():
    keyword = request.args.get('keyword')  # Get the keyword from query parameters
    notes = find_notes(keyword)  # Call the service layer to find notes matching the keyword
   # Convert ObjectId to string for JSON serialization
    for note in notes:
        note['_id'] = str(note['_id'])
    return jsonify(notes), 200  # Return the list of matching notes with HTTP 200 status
