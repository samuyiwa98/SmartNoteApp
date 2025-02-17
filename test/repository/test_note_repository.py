import pytest
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from repository.note_repository import add_note, get_all_notes, update_note, delete_note
from model.note import Note

@pytest.fixture
def db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.test_note_app
    yield db
    client.drop_database(db)

def test_add_note_with_empty_content(db):
    note = Note("", "", "Work")
    result = add_note(note, db)
    assert result.inserted_id is not None

def test_update_note_with_nonexistent_id(db):
    updated_note = {"title": "Updated Title", "content": "Updated Content", "category": "Personal"}
    update_result = update_note('nonexistent_id', updated_note, db)
    assert update_result.modified_count == 0

def test_delete_note_with_nonexistent_id(db):
    delete_result = delete_note('nonexistent_id', db)
    assert delete_result.deleted_count == 0

def test_db_connection_failure():
    with pytest.raises(ConnectionFailure):
        client = MongoClient('mongodb://invalid_host:27017/')
        client.server_info()  # This should raise a ConnectionFailure
