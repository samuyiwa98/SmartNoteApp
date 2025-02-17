"""
This module is responsible for analyzing the sentiment of user input text using the TextBlob library.
It provides a function to calculate the sentiment polarity of a given text, which can be used to determine the overall sentiment as positive, negative, or neutral.

The module assumes that the TextBlob library is installed and available in the environment. It is designed to be simple and efficient, providing a quick way to assess the sentiment of textual content.
"""

from textblob import TextBlob
# from tags import NoteTag

"Analyse sentiment of th user input"
def analyze_sentiment(content):
    blob = TextBlob(content)
    return blob.sentiment.polarity
    
