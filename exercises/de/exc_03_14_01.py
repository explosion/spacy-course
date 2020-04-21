import json
import spacy

nlp = spacy.load("de_core_news_sm")

with open("exercises/de/tweets.json") as f:
    TEXTS = json.loads(f.read())

# Verarbeite den Text und drucke die Nomen
for text in TEXTS:
    doc = nlp(text)
    print([token.text for token in doc if token.pos_ == "NOUN"])
