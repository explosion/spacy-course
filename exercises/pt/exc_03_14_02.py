import json
import spacy

nlp = spacy.load("pt_core_news_sm")

with open("exercises/pt/tweets.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

# Processar os textos e imprimir as entidades
docs = [nlp(text) for text in TEXTS]
entities = [doc.ents for doc in docs]
print(*entities)
