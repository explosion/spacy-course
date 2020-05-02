from spacy.lang.en import English

nlp = English()

# Import the Doc and Span classes
from spacy.____ import ____, ____

words = ["I", "like", "David", "Bowie"]
spaces = [True, True, True, False]

# Create a doc from the words and spaces
doc = ____(____, ____, ____)
print(doc.text)

# Create a span for "David Bowie" from the doc and assign it the label "PERSON"
span = ____(____, ____, ____, label=____)
print(span.text, span.label_)

# Add the span to the doc's entities
____.____ = [____]

# Print entities' text and labels
print([(ent.text, ent.label_) for ent in doc.ents])
