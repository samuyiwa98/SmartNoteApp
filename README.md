# SmartNoteApp

Smart Note Organizer is a powerful and intuitive application designed to help users manage their notes efficiently. With a combination of core functionalities and AI-powered features, this app ensures that your notes are always organized and easily accessible.

# Core Features
•	Add, Edit, Delete, and View Notes: Users can effortlessly create, modify, remove, and view their notes.

•	Categorize Notes: Users can assign categories to notes such as Work, Personal, Ideas, etc., to keep them organized.

•	Search Functionality: Users can quickly find notes based on keywords, making it easy to locate specific information.

# AI Features
•	Automatic Categorization: The app suggests/assigns categories to notes based on their content using the scikit-learn library.

•	Sentiment Analysis: The app can also detect and display the sentiment of the note (e.g., Positive, Neutral, Negative) to provide insights into the tone of your notes.

# Prerequisites
•	Python 3.8 or higher

•	MongoDB

•	pip


# Why MongoDB?

MongoDB was chosen for the backend implementation due to several reasons:

1. **Flexibility:** MongoDB is a NoSQL database, which means it can handle unstructured data and allows for flexible schema design. This is particularly useful for a note-taking application where the structure of notes can vary.
   
2. **Scalability:** MongoDB is designed to scale horizontally, making it suitable for applications that need to handle large volumes of data and high traffic.
   
3. **Ease of Use:** MongoDB's document-oriented storage makes it easy to store and retrieve JSON-like documents, which aligns well with the structure of notes.
   
4. **Rich Query Language:** MongoDB provides a powerful query language that supports a wide range of operations, including filtering, sorting, and aggregations, which are essential for implementing search functionality.

5. **Integration with Python:** The pymongo library provides a seamless integration between MongoDB and Python, making it easy to interact with the database from the Flask application.


# Libraries Used

•	**Flask:** For creating the web application.

•	**pymongo:** For interacting with MongoDB.

•	**textblob:** For sentiment analysis.

•	**scikit-learn:** For training machine learning models.

•	**pandas:** For data manipulation and analysis.

•	**joblib:** For model serialization.

•	**bson:** For working with BSON data.

•       **unittest.mock:** For mocking and patching objects during testing, allowing for isolation of the code under test.


# Tools & Frameworks

This application leverages a variety of tools and frameworks to deliver robust functionality and maintainability. Below is a detailed list of the key technologies used:

**Backend Framework**

**Flask:** A lightweight WSGI web application framework in Python. It is designed with simplicity and flexibility in mind, making it ideal for building web applications and APIs.

**Database**

**MongoDB:** A NoSQL database known for its scalability and flexibility. It stores data in JSON-like documents, allowing for dynamic schemas.

**PyMongo:** The official MongoDB driver for Python, used to interact with MongoDB databases.


**Machine Learning**

**scikit-learn:** A machine learning library in Python that provides simple and efficient tools for data mining and data analysis. It's used for training and deploying the categorization model.

**joblib:** A library for lightweight pipelining in Python, used to serialize and deserialize the trained machine learning model.

**Testing**

**pytest:** A testing framework that makes building simple and scalable test cases easy. It supports fixtures, parameterized testing, and more.

**unittest.mock:** A library for mocking objects during testing, allowing for isolation of the code under test.

**pytest-cov:** A plugin for measuring code coverage, ensuring that all critical paths are tested.

**Utilities**

**TextBlob:** A Python library for processing textual data, used for sentiment analysis in the application.

**Development and Deployment**

**Virtualenv:** A tool to create isolated Python environments, ensuring that dependencies are managed separately for each project.


# Project Structure

The project has a well-defined structure which is crucial for maintainability, scalability, and collaboration.

• **app.py:** The main entry point of the application. It initializes the Flask app, configures extensions like JWT, and registers blueprints.

• **config/:** Contains configuration files. config.py holds settings such as database URIs, secret keys, and other environment-specific configurations.

• **controllers/:** Manages the routing and handling of HTTP requests. note_controller.py defines endpoints related to note operations.

• **models/:** Defines the data structures used in the application. note.py defines a Note class representing the note entity.

• **repositories/:** Handles data access logic, interacting with the database. note_repository.py contains functions for CRUD operations on notes.

• **services/:** Contains business logic and application services. note_service.py implements the core logic for note management, such as creating, updating, and deleting notes.

• **utils/:** Utility functions and helpers. sentiment_analysis.py and categorisation.py provide functions for sentiment analysis and category prediction, respectively.

• **ml/:** Machine learning components. train_model.py is used to train and save the model, while note_categorizer.pkl stores the serialized model.

• **data/:** Stores datasets used for training and evaluation. notes_dataset.csv contains labeled data for training the categorization model.

• **tests/:** Contains test cases to ensure application functionality. test_notes.py includes tests for note-related features, and conftest.py sets up fixtures for testing.

• **venv/:** The virtual environment directory, which contains installed dependencies specific to the project.



**Benefits of This Structure:**

• **Modularity:** Each component of the application is separated into its own directory, making it easier to manage and understand.

• **Scalability:** The structure supports growth, allowing new features and components to be added without disrupting existing functionality.

• **Maintainability:** Clear separation of concerns ensures that changes in one part of the application do not inadvertently affect others.

• **Collaboration:** A well-organized structure facilitates collaboration among team members, as responsibilities and code locations are clearly defined.

<img width="223" alt="image" src="https://github.com/user-attachments/assets/dee38aed-6bc8-4183-ae17-655d9a05a4ff" />


# Setup

1.	Clone the repository:
   
    • git clone https://github.com/yourusername/smart-note-organizer.git
  	
2.	Navigate to the project directory:
   
    • cd smart-note-organizer
  	
3.	Create a virtual environment:
	
    • python -m venv venv
  	
4.	Activate the virtual environment:
   
    •	On Windows: bash venv\Scripts\activate

    •	On macOS/Linux: bash source venv/bin/activate

5.	Install dependencies:
    
     	pip install -r requirements.txt

  	
  		pip install pytest pytest-cov
  	

7.	Configure MongoDB
   
8.	Initialise the Database
    
     • python init_db.py
   
9.	Train the Model (Optional)


# CSV Data

The notes.csv file contains the data used for training the machine learning models. It includes the following columns:

•	**content:** Content of the note.

•	**category:** Category assigned to the note (e.g., Work, Personal, Ideas).

**Example CSV Data:**

Discuss project milestones and deadlines, Work

Buy milk, eggs, and bread, Personal

Develop an app for note organization, Ideas


# Train Model Class

The train_model.py script is used to train the machine learning models for automatic categorization and sentiment analysis.

Example Code:

<img width="869" alt="image" src="https://github.com/user-attachments/assets/dd2afcce-2fdd-4efe-a333-df09bf01125b" />



# Usage
1.	Start the Flask application:
   
   	• Python app.py
  	
(To access the application you can use the postman collection provided to test the endpoint)
   
Note: Make sure you are in your virtual environment and in the root directory of the project.


# APIs

1. Create a Note
   
  •	Endpoint: /notes

  •	Method: POST

  •	Description: Allows the user to create a new note.


  •	Example Request Body:


<img width="196" alt="image" src="https://github.com/user-attachments/assets/324ec813-1264-4bdb-ba85-d35dd2bee68a" />


Note: Category can be left empty by the user and the application will suggest a category.



2. Get All Notes
   
  •	Endpoint: /notes/all

  •	Method: GET

  •	Description: Enables the user to retrieve all notes.



3. Get a Note by ID
   
  •	Endpoint: /notes/<id>

  •	Method: GET

  •	Description: Enables the user to retrieve a note by its ID.



4. Update a Note
   
  •	Endpoint: /notes/update/<id>

  •	Method: PUT

  •	Description: User can update an existing note.

  •	Request Body:


<img width="352" alt="image" src="https://github.com/user-attachments/assets/d7f784e4-ba1a-44c0-8245-38b39aa03fa0" />



5. Delete a Note
   
  •	Endpoint: /notes/remove/<id>

  •	Method: DELETE

  •	Description: User can delete a note by its ID.



6. Search Notes
   
  •	Endpoint: /notes/search

  •	Method: GET

  •	Description: User can search for notes based on keywords.

  •	Query Parameters

<img width="523" alt="image" src="https://github.com/user-attachments/assets/eb4366de-bbf5-4d6c-85e4-334f35457094" />

# Testing

This project employs a robust testing strategy to ensure the reliability and correctness of the application. We use pytest as our primary testing framework, which allows for easy test discovery and execution. The tests cover various layers of the application, including the service layer, repository layer, controller layer, and database interactions.

Testing Approach:

**Unit Testing**: Focuses on individual components, such as functions and methods, to ensure they work as expected in isolation. Mocking is extensively used to simulate external dependencies.

**Integration Testing:** Verifies that different components of the application work together correctly. These tests often involve real database interactions to ensure data integrity.

**Edge Case Testing:** Includes tests for handling unexpected or extreme inputs to ensure the application behaves gracefully under all conditions.

**Regression Testing:** Ensures that new changes do not adversely affect existing functionality. This is achieved by running the full test suite after each significant change.


Running the tests:

1. Activate the Virtual Environment: Before running the tests, ensure your virtual environment is activated.

	source venv/bin/activate

2. Navigate to the Project Directory: Ensure you are in the root directory of the project where the tests directory is located.

	cd /path/to/your/SNotes_app


3. Execute the Test Suite: Run the entire test suite using pytest. This command will automatically discover and execute all test files in the tests directory.

	pytest tests/

4. Generate a Coverage Report: To ensure comprehensive test coverage, you can generate a coverage report using pytest-cov.

	pytest --cov=your_module tests/

Replace your_module with the name of the module you want to measure coverage for.


# Future Enhancements

1. **Authentication**: Implement authentication using Flask-JWT-Extended to secure your API endpoints.

2. **Logging:** Add logging to capture request details and predictions for monitoring and debugging.

3. **Batch Predictions**: Extend the API to handle batch predictions, allowing multiple notes to be categorized in a single request.

4. **Model Updates:** Implement a mechanism to update the model periodically with new data to improve accuracy and adapt to changing trends.

5. **Advanced Models:** Consider using more advanced models like BERT or GPT for improved categorization accuracy.

6. **Error Handling:** Implement more robust error handling in your Flask application to provide informative error messages for common issues.

7. **Automated Testing:** Include automated tests for your API endpoints to ensure they work as expected and handle edge cases.

8. **Continuous Integration:** Integrate the tests into a CI/CD pipeline to ensure that they are run automatically on code changes.

9. **Mocking External Dependencies:** Use mocking to simulate external dependencies and isolate the tests.

10. **Performance Testing:** Consider adding performance tests to ensure the application can handle high loads.



