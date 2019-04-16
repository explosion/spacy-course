import json
import spacy

nlp = spacy.load("en_core_web_sm")

with open("exercises/tweets.json") as f:
    TEXTS = json.loads(f.read())

# Process the texts and print the entities
docs = list(nlp.pipe(TEXTS))
entities = [doc.ents for doc in docs]
print(*entities)
