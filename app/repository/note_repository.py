"""
This module is responsible for interacting with a MongoDB database to perform CRUD (Create, Read, Update, Delete) operations on a collection of notes.
It utilizes the PyMongo library to connect to the database and execute operations on the notes collection.

Key Responsibilities:
- **Database Connection**: Establishes a connection to the MongoDB database using a URI specified in the configuration file.
- **Add Note**: Inserts a new note document into the notes collection.
- **Get All Notes**: Retrieves all note documents from the notes collection.
- **Update Note**: Updates an existing note document identified by its unique ID.
- **Delete Note**: Deletes a note document from the collection based on its unique ID.
- **Search Notes**: Performs a text search on the notes collection to find documents matching a specified keyword.

The module assumes that the MongoDB server is running and accessible via the provided URI.
It also assumes that the notes collection is properly indexed for text search to enable efficient keyword-based queries.
"""

from pymongo import MongoClient
from config.config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.notes_db
notes_collection = db.notes

def add_note(note):
    return notes_collection.insert_one(note.__dict__)

def get_all_notes():
    return list(notes_collection.find())

def get_note_by_id(note_id):
    return notes_collection.find_one({"_id": note_id})

def update_note(note_id, updated_note):
    return notes_collection.update_one({'_id': note_id}, {'$set': updated_note})

def delete_note(note_id):
    return notes_collection.delete_one({'_id': note_id})

def search_notes(keyword):
    return list(notes_collection.find({"$text": {"$search": keyword}}))


