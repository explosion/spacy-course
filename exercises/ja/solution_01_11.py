import spacy

# Matcherをインポート
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")

# 共有語彙データを用いてMatcherを初期化
matcher = Matcher(nlp.vocab)

# 「iPhone」と「X」にマッチするパターンを作成
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]

# matcherにパターンを追加
matcher.add("IPHONE_X_PATTERN", None, pattern)

# docに対してmatcherを用いる
matches = matcher(doc)
print("Matches:", [doc[start:end].text for match_id, start, end in matches])
