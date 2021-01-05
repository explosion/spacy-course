import json
import spacy

nlp = spacy.load("en_core_web_sm")

with open("exercises/en/tweets.json") as f:
    TEXTS = json.loads(f.read())

# Processar os textos e imprimir as entidades
docs = list(nlp.pipe(TEXTS))
entities = [doc.ents for doc in docs]
print(*entities)
