import json
import spacy

nlp = spacy.load("fr_core_news_sm")

with open("exercises/fr/tweets.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

# Traite les textes et affiche les adjectifs
for doc in nlp.pipe(TEXTS):
    print([token.text for token in doc if token.pos_ == "ADJ"])
