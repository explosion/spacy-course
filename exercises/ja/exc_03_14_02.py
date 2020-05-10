import json
import spacy

nlp = spacy.load("en_core_web_sm")

with open("exercises/en/tweets.json") as f:
    TEXTS = json.loads(f.read())

# テキストを処理し、固有表現をプリント
docs = [nlp(text) for text in TEXTS]
entities = [doc.ents for doc in docs]
print(*entities)
