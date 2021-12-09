import json
import spacy
from spacy.matcher import Matcher

with open("exercises/ja/iphone.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = spacy.blank("ja")
matcher = Matcher(nlp.vocab)

# 小文字が"iphone"と"x"にマッチする2つのトークン
pattern1 = [{____: ____}, {____: ____}]

# 小文字が"iphone"と数字にマッチする2つのトークン
pattern2 = [{____: ____}, {____: ____}]

# パターンをmatcherに追加して、結果をチェックする
matcher.add("GADGET", None, pattern1, pattern2)
for doc in nlp.pipe(TEXTS):
    print([doc[start:end] for match_id, start, end in matcher(doc)])
