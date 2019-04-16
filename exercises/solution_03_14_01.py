import json
import spacy

nlp = spacy.load("en_core_web_sm")

with open("exercises/tweets.json") as f:
    TEXTS = json.loads(f.read())

# Process the texts and print the adjectives
for doc in nlp.pipe(TEXTS):
    print([token.text for token in doc if token.pos_ == "ADJ"])
