"""
This module is responsible for managing note operations, providing a high-level interface for creating, retrieving, updating, deleting, and searching notes.

Key Responsibilities:
- **Create Note**: Constructs a new note with a title, content, and optional category. It analyzes the sentiment of the content and suggests a category if none is provided, before saving the note to the repository.
- **List Notes**: Retrieves all notes from the repository, providing a complete list of stored notes.
- **Modify Note**: Updates an existing note's title, content, category, and sentiment by its unique ID, reflecting changes in the repository.
- **Remove Note**: Deletes a note from the repository based on its unique ID.
- **Find Notes**: Searches for notes containing a specified keyword, utilizing the repository's search capabilities.

The module assumes the existence of a `Note` model class, repository functions for database interactions, and utility functions for sentiment analysis and category suggestion.
It abstracts the complexity of these operations, offering a simplified interface for note management.
"""
from model.note import Note
from repository.note_repository import add_note, get_all_notes, get_note_by_id ,update_note, delete_note, search_notes
from utils.sentiment_analysis import analyze_sentiment
from utils.categorisation import suggest_category

def create_note(title, content, category=None):
    sentiment = analyze_sentiment(content)
    if not category:
        category = suggest_category(content)
    note = Note(title, content, category, sentiment)
    return add_note(note)

def list_notes():
    return get_all_notes()

def note_by_id(note_id):
    return get_note_by_id()

def modify_note(note_id, title, content, category):
    sentiment = analyze_sentiment(content)
    updated_note = {
        "title": title,
        "content": content,
        "category": category,
        "sentiment": sentiment
    }
    return update_note(note_id, updated_note)

def remove_note(note_id):
    return delete_note(note_id)

def find_notes(keyword):
    return search_notes(keyword)
