import json
import spacy

nlp = spacy.load("en_core_web_sm")

with open("exercises/en/tweets.json") as f:
    TEXTS = json.loads(f.read())

# テキストを処理し、形容詞をプリント
for doc in nlp.pipe(TEXTS):
    print([token.text for token in doc if token.pos_ == "ADJ"])
