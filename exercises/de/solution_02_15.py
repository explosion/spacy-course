import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
import json

with open("exercises/de/countries.json") as f:
    COUNTRIES = json.loads(f.read())
with open("exercises/de/country_text.txt") as f:
    TEXT = f.read()

nlp = spacy.load("de_core_news_sm")
matcher = PhraseMatcher(nlp.vocab)
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", None, *patterns)

# Erstelle ein Doc und setze die vorhandenen Entitäten zurück
doc = nlp(TEXT)
doc.ents = []

# Iteriere über die Resultate
for match_id, start, end in matcher(doc):
    # Erstelle eine Span mit dem Label "LOC"
    span = Span(doc, start, end, label="LOC")

    # Überschreibe die doc.ents und füge die Span hinzu
    doc.ents = list(doc.ents) + [span]

    # Wähle den Kopf-Token des Root-Tokens der Span aus
    span_root_head = span.root.head
    # Drucke den Text des Kopf-Tokens und den Text der Span
    print(span_root_head.text, "-->", span.text)

# Drucke die Entitäten im Dokument
print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "LOC"])
