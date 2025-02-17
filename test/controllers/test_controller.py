import pytest
from bson import ObjectId
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_create_note(client, db):
    response = client.post('/notes', json={
        'title': 'Test Note',
        'content': 'This is a test note.',
        'category': 'test'
    })
    assert response.status_code == 201
    data = response.get_json()
    note_id = data['inserted_id']
    note = db.notes.find_one({'_id': ObjectId(note_id)})
    assert note is not None
    assert note['title'] == 'Test Note'
    assert note['content'] == 'This is a test note.'
    assert note['category'] == 'test'  # Ensure category is assigned

def test_create_note_without_category(client, db):
    response = client.post('/notes', json={
        'title': 'Test Note',
        'content': 'This is a test note.'
    })
    assert response.status_code == 201
    data = response.get_json()
    note_id = data['inserted_id']
    note = db.notes.find_one({'_id': ObjectId(note_id)})
    assert note is not None
    assert note['title'] == 'Test Note'
    assert note['content'] == 'This is a test note.'
    assert note['category'] is not None  # Ensure category is automatically assigned

def test_edit_note_content(client, db):
    # Create a note first
    response = client.post('/notes', json={
        'title': 'Editable Note',
        'content': 'Original content.'
    })
    note_id = response.get_json()['inserted_id']

    # Edit the note
    response = client.put(f'/notes/{note_id}', json={
        'title': 'Editable Note',
        'content': 'Updated content.',
        'category': 'Ideas'
    })
    assert response.status_code == 200
    note = db.notes.find_one({'_id': ObjectId(note_id)})
    assert note['content'] == 'Updated content.'

def test_delete_note(client, db):
    # Create a note first
    response = client.post('/notes', json={
        'title': 'Deletable Note',
        'content': 'This note will be deleted.'
    })
    note_id = response.get_json()['inserted_id']

    # Delete the note
    response = client.delete(f'/notes/{note_id}')
    assert response.status_code == 200
    note = db.notes.find_one({'_id': ObjectId(note_id)})
    assert note is None

def test_add_note_missing_content(client):
    response = client.post('/notes', json={
        'title': 'Test Note'
    })
    assert response.status_code == 400
    assert response.get_json() == {"error": "Content is required"}

def test_get_notes_empty_db(client):
    response = client.get('/notes')
    assert response.status_code == 200
    assert response.get_json() == []

