# config/config.py
import os
from urllib.parse import quote_plus

# Retrieve MongoDB credentials from environment variables
username = os.environ.get('MONGO_USER')
password = os.environ.get('MONGO_PASS')
host = os.environ.get('MONGO_HOST', '@cluster0.blesiqx.mongodb.net')
dbname = os.environ.get('MONGO_DBNAME', 'SmartNoteAppDb')

# Encode the username and password
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)

# Construct the MongoDB URI
MONGO_URI = f"mongodb+srv://{encoded_username}:{encoded_password}@{host}/{dbname}?retryWrites=true&w=majority"
