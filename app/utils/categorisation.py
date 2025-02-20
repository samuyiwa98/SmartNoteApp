"""
This module is responsible for loading a pre-trained machine learning model and using it to suggest categories for note content.
It leverages the joblib library to load the model and provides a function to predict the category of a given text input.

Key Responsibilities:
- **Model Loading**: Loads the trained model from a specified file path at the module level to ensure it is loaded only once, optimizing performance by avoiding repeated loading.
- **Category Suggestion**: Uses the loaded model to predict and suggest a category for the given content. If the model is not loaded successfully, it returns 'Unknown' as a fallback.

The module includes error handling to manage common issues such as missing or corrupted model files, providing informative messages to guide the user.
It assumes that the model file is located in the 'ml' directory and is named 'note_categorizer.pkl'.
"""

import joblib
import os

# Define the path to the model file
MODEL_PATH = os.path.join(os.path.dirname(__file__),'ml', 'note_categorizer.pkl')

def load_model():
    """
    Load the trained model from the specified file path.

    Returns:
        model: The loaded model if successful, None otherwise.
    """
    try:
        # Load the trained model
        model = joblib.load(MODEL_PATH)
        print("Model loaded successfully.")
        return model
    except FileNotFoundError:
        print(f"Error: The model file '{MODEL_PATH}' was not found.")
        return None
    except EOFError:
        print("Error: The model file is incomplete or corrupted.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Load the model once at module level to avoid repeated loading
model = load_model()

def suggest_category(content):
    """
    Suggest a category for the given content using the trained model.

    Args:
        content (str): The content of the note.

    Returns:
        str: The suggested category, or 'Unknown' if the model is not loaded.
    """
    if model:
        try:
            return model.predict([content])[0]
        except Exception as e:
            print(f"Prediction error: {e}")
            return 'Unknown'
    else:
        return 'Unknown'

