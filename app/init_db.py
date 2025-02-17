
"""
This module is responsible for creating a text index on the 'title' and 'content' fields of the notes collection in a MongoDB database.
Text indexing is essential for enabling efficient text search capabilities, allowing for fast and accurate retrieval of documents based on textual queries.

The module assumes that the MongoDB server is running and accessible via the provided URI, and that the notes collection exists within the specified database.

"""
from pymongo import MongoClient
from config.config import MONGO_URI

def create_text_index():
    # Connect to MongoDB
    client = MongoClient(MONGO_URI)
    db = client.notes_db

    # Create a text index on the 'title' and 'content' fields
    db.notes.create_index([('title', 'text'), ('content', 'text')])

    print("Text index created successfully.")

if __name__ == '__main__':
    create_text_index()
