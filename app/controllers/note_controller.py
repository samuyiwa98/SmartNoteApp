from flask import Blueprint, request, jsonify
from bson import ObjectId
from service.note_service import create_note, list_notes, note_by_id, modify_note, remove_note, find_notes

# Create a Blueprint for the notes, which allows us to organize the routes related to notes
note_bp = Blueprint('note_bp', __name__)

@note_bp.route('/notes', methods=['POST'])
def add_note():
    data = request.json
    result = create_note(data['title'], data['content'], data['category'])
    return jsonify({"inserted_id": str(result.inserted_id)}), 201

@note_bp.route('/notes/all', methods=['GET'])
def get_notes():
    notes = list_notes()
    # Convert ObjectId to string for JSON serialization
    for note in notes:
        note['_id'] = str(note['_id'])
    return jsonify(notes), 200

@note_bp.route('/notes/<note_id>', methods=['GET'])
def get_notes_by_id(note_id):
    try:
        note_id = ObjectId(note_id)
    except Exception:
        return jsonify({"error": "Invalid note ID format"}), 400
    note = note_by_id(note_id)
    if note:
        note['_id'] = str(note['_id'])
        return jsonify(note), 200
    else:
        return jsonify({"error": "Note not found"}), 404

@note_bp.route('/notes/update/<note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.json
    try:
        note_id = ObjectId(note_id)
    except Exception:
        return jsonify({"error": "Invalid note ID format"}), 400

    result = modify_note(note_id, data['title'], data['content'], data['category'])
    return jsonify({"modified_count": result.modified_count}), 200

@note_bp.route('/notes/remove/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    try:
        note_id = ObjectId(note_id)
    except Exception:
        return jsonify({"error": "Invalid note ID format"}), 400
    result = remove_note(note_id)
    return jsonify({"deleted_count": result.deleted_count}), 200

@note_bp.route('/notes/search', methods=['GET'])
def search_notes():
    keyword = request.args.get('keyword')
    notes = find_notes(keyword)
    # Convert ObjectId to string for JSON serialization
    for note in notes:
        note['_id'] = str(note['_id'])
    return jsonify(notes), 200
