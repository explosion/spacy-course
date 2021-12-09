import json
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span

with open("exercises/ja/iphone.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = spacy.blank("ja")
matcher = Matcher(nlp.vocab)

# 小文字が"iphone"と"x"にマッチする2つのトークン
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]

# 小文字が"iphone"と数字にマッチする2つのトークン
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]

# パターンをmatcherに追加して、結果をチェックする
matcher.add("GADGET", [pattern1, pattern2])
docs = []
for doc in nlp.pipe(TEXTS):
    matches = matcher(doc)
    spans = [Span(doc, start, end, label=match_id) for match_id, start, end in matches]
    print(spans)
    doc.ents = spans
    docs.append(doc)

