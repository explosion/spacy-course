import json
import spacy

nlp = spacy.load("de_core_news_sm")

with open("exercises/de/tweets.json") as f:
    TEXTS = json.loads(f.read())

# Verarbeite den Text und drucke die Entitäten
docs = [nlp(text) for text in TEXTS]
entities = [doc.ents for doc in docs]
print(*entities)
