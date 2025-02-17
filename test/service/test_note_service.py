import pytest
from unittest.mock import patch, MagicMock
from service.note_service import create_note, modify_note, remove_note
from model.note import Note


def test_create_note_with_valid_data():
    with patch('service.note_service.add_note') as mock_add_note:
        mock_add_note.return_value = MagicMock(inserted_id='12345')
        result = create_note("Test Title", "Test Content", "Work")
        mock_add_note.assert_called_once()
        assert result.inserted_id == '12345'

def test_create_note_without_category():
    with patch('service.note_service.add_note') as mock_add_note, \
         patch('utils.categorisation.suggest_category', return_value="Ideas"):
        mock_add_note.return_value = MagicMock(inserted_id='12345')
        result = create_note("Test Title", "Test Content")
        mock_add_note.assert_called_once()
        assert result.inserted_id == '12345'

def test_create_note_with_empty_title():
    with patch('service.note_service.add_note') as mock_add_note:
        result = create_note("", "Test Content", "Work")
        mock_add_note.assert_not_called()
        assert result is None


def test_create_note_with_invalid_data():
    with patch('service.note_service.add_note') as mock_add_note:
        mock_add_note.return_value = MagicMock(inserted_id=None)
        result = create_note("", "", None)
        mock_add_note.assert_not_called()
        assert result is None

def test_modify_note_with_valid_data():
    with patch('service.note_service.update_note') as mock_update_note:
        mock_update_note.return_value = MagicMock(modified_count=1)
        result = modify_note('12345', "Updated Title", "Updated Content", "Personal")
        mock_update_note.assert_called_once()
        assert result.modified_count == 1        

def test_modify_note_with_nonexistent_id():
    with patch('service.note_service.update_note') as mock_update_note:
        mock_update_note.return_value = MagicMock(modified_count=0)
        result = modify_note('nonexistent_id', "Title", "Content", "Category")
        mock_update_note.assert_called_once()
        assert result.modified_count == 0

def test_remove_note_with_valid_id():
    with patch('service.note_service.delete_note') as mock_delete_note:
        mock_delete_note.return_value = MagicMock(deleted_count=1)
        result = remove_note('12345')
        mock_delete_note.assert_called_once()
        assert result.deleted_count == 1

def test_remove_note_with_nonexistent_id():
    with patch('service.note_service.delete_note') as mock_delete_note:
        mock_delete_note.return_value = MagicMock(deleted_count=0)
        result = remove_note('nonexistent_id')
        mock_delete_note.assert_called_once()
        assert result.deleted_count == 0
