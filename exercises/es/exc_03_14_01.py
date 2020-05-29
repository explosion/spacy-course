import json
import spacy

nlp = spacy.load("es_core_news_sm")

with open("exercises/es/tweets.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

# Procesa los textos e imprime los adjetivos en pantalla
for text in TEXTS:
    doc = nlp(text)
    print([token.text for token in doc if token.pos_ == "NOUN"])
