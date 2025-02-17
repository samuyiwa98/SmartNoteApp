"""
The train_model.py script is responsible for training a machine learning model to categorize notes based on their textual content.
It leverages the Scikit-learn library to create a text classification pipeline using TF-IDF vectorization and a Multinomial Naive Bayes classifier.
The script is designed to load a dataset, preprocess the data, train the model, evaluate its performance, and save the trained model for future use.

Key Responsibilities:
- **Dataset Loading**: Loads the dataset from a CSV file located in the 'data' directory. It handles errors related to file not found, empty data, and other unexpected issues.
- **Data Preprocessing**: Ensures that the dataset contains the required 'content' and 'category' columns necessary for training.
- **Data Splitting**: Splits the dataset into training and testing sets to evaluate the model's performance.
- **Model Training**: Constructs a machine learning pipeline that includes TF-IDF vectorization and a Multinomial Naive Bayes classifier, and trains it on the training data.
- **Model Evaluation**: Evaluates the trained model on the test data and prints the accuracy score to assess its performance.
- **Model Saving**: Saves the trained model to a file in the 'ml' directory using the joblib library, allowing it to be loaded and used for predictions in the future.

The script is designed to be executed as a standalone program, with the main function `train_and_save_model` encapsulating the entire process.
It provides informative print statements to guide the user through each step, ensuring clarity and ease of use.
"""


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

def train_and_save_model():
    # Define the path to the dataset
    dataset_path = os.path.join('data', 'notes.csv')

    # Load the dataset
    try:
        data = pd.read_csv(dataset_path)
        print("Dataset loaded successfully.")
    except FileNotFoundError:
        print(f"Error: The dataset file '{dataset_path}' was not found.")
        return
    except pd.errors.EmptyDataError:
        print("Error: The dataset file is empty.")
        return
    except Exception as e:
        print(f"An unexpected error occurred while loading the dataset: {e}")
        return

    # Print the columns of the DataFrame
    print("Columns in the dataset:", data.columns.tolist())

    # Check if the required columns are present
    if 'content' not in data.columns or 'category' not in data.columns:
        print("Error: The dataset must contain 'content' and 'category' columns.")
        return

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data['content'], data['category'], test_size=0.2, random_state=42)

    # Create a pipeline that combines the TfidfVectorizer and MultinomialNB
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate the model
    predicted_categories = model.predict(X_test)
    accuracy = accuracy_score(y_test, predicted_categories)
    print(f"Model Accuracy: {accuracy:.2f}")

    # Save the trained model
    model_path = os.path.join('ml', 'note_categorizer.pkl')
    joblib.dump(model, model_path)
    print(f"Model saved to '{model_path}'.")

if __name__ == '__main__':
    train_and_save_model()
