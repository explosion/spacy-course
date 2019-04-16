import json
from spacy.lang.en import English
from spacy.tokens import Doc

with open("exercises/bookquotes.json") as f:
    DATA = json.loads(f.read())

nlp = English()

# Register the Doc extension 'author' (default None)
Doc.set_extension("author", default=None)

# Register the Doc extension 'book' (default None)
Doc.set_extension("book", default=None)

for doc, context in nlp.pipe(DATA, as_tuples=True):
    # Set the doc._.book and doc._.author attributes from the context
    doc._.book = context["book"]
    doc._.author = context["author"]

    # Print the text and custom attribute data
    print(doc.text, "\n", "— '{}' by {}".format(doc._.book, doc._.author), "\n")
