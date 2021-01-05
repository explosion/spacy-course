import json
from spacy.matcher import Matcher
from spacy.lang.ja import Japanese

with open("exercises/ja/iphone.json") as f:
    TEXTS = json.loads(f.read())

nlp = Japanese()
matcher = Matcher(nlp.vocab)

# 小文字が"iphone"と"x"にマッチする2つのトークン
pattern1 = [{____: ____}, {____: ____}]

# 小文字が"iphone"と数字にマッチする2つのトークン
pattern2 = [{____: ____}, {____: ____}]

# パターンをmatcherに追加して、結果をチェックする
matcher.add("GADGET", None, pattern1, pattern2)
for doc in nlp.pipe(TEXTS):
    print([doc[start:end] for match_id, start, end in matcher(doc)])
