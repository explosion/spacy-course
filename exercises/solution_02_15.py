from spacy.lang.en import English
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
import json

with open("exercises/countries.json") as f:
    COUNTRIES = json.loads(f.read())
with open("exercises/country_text.txt") as f:
    TEXT = f.read()

nlp = English()
matcher = PhraseMatcher(nlp.vocab)
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", None, *patterns)

# Create a doc and find matches in it
doc = nlp(TEXT)

# Iterate over the matches
for match_id, start, end in matcher(doc):
    # Create a Span with the label for "GPE"
    span = Span(doc, start, end, label="GPE")

    # Overwrite the doc.ents and add the span
    doc.ents = list(doc.ents) + [span]

    # Get the span's root head token
    span_root_head = span.root.head
    # Print the text of the span root's head token and the span text
    print(span_root_head.text, "-->", span.text)

# Print the entities in the document
print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "GPE"])
