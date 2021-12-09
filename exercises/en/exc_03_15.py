import json
import spacy
from spacy.tokens import Doc

with open("exercises/en/bookquotes.json", encoding="utf8") as f:
    DATA = json.loads(f.read())

nlp = spacy.blank("en")

# Register the Doc extension "author" (default None)
____

# Register the Doc extension "book" (default None)
____

for doc, ____ in ____(____, ____):
    # Set the doc._.book and doc._.author attributes from the context
    doc._.book = ____
    doc._.author = ____

    # Print the text and custom attribute data
    print(f"{doc.text}\n — '{doc._.book}' by {doc._.author}\n")
