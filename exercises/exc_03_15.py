import json
from spacy.lang.en import English
from spacy.tokens import Doc

with open("exercises/bookquotes.json") as f:
    DATA = json.loads(f.read())

nlp = English()

# Register the Doc extension 'author' (default None)
____

# Register the Doc extension 'book' (default None)
____

for doc, ____ in ____(____, ____):
    # Set the doc._.book and doc._.author attributes from the context
    doc._.book = ____
    doc._.author = ____

    # Print the text and custom attribute data
    print(doc.text, "\n", "— '{}' by {}".format(doc._.book, doc._.author), "\n")
