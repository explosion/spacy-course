import json
import spacy

nlp = spacy.load("fr_core_news_sm")

with open("exercises/fr/tweets.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

# Traite les textes et affiche les entités
docs = list(nlp.pipe(TEXTS))
entities = [doc.ents for doc in docs]
print(*entities)
