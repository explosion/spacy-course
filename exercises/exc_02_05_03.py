import spacy

nlp = spacy.load("en_core_web_sm")

# Import the Doc class
from ____ import ____

# Desired text: "Oh, really?!"
words = [____, ____, ____, ____, ____]
spaces = [____, ____, ____, ____, ____]

# Create a Doc from the words and spaces
doc = ____(____, ____=____, ____=____)
print(doc.text)
