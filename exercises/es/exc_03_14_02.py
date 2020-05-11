import json
import spacy

nlp = spacy.load("en_core_web_sm")

with open("exercises/en/tweets.json") as f:
    TEXTS = json.loads(f.read())

# Procesa los textos e imprime las entidades en pantalla
docs = [nlp(text) for text in TEXTS]
entities = [doc.ents for doc in docs]
print(*entities)
