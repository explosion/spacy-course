import json
import spacy

nlp = spacy.load("ja_core_news_sm")

with open("exercises/ja/tweets.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

# テキストを処理し、固有表現を表示
docs = list(nlp.pipe(TEXTS))
entities = [doc.ents for doc in docs]
print(*entities)
