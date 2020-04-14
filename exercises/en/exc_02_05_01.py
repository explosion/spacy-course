import spacy

nlp = spacy.load("en_core_web_sm")

# Import the Doc class
from ____ import ____

# Desired text: "spaCy is cool!"
words = ["spaCy", "is", "cool", "!"]
spaces = [True, True, False, False]

# Create a Doc from the words and spaces
doc = ____(____, words=words, spaces=spaces)
print(doc.text)
