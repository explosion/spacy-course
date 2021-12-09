import json
import spacy

nlp = spacy.load("ja_core_news_sm")

with open("exercises/ja/tweets.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

# テキストを処理し、形容詞を表示
for text in TEXTS:
    doc = nlp(text)
    print([token.text for token in doc if token.pos_ == "ADJ"])
