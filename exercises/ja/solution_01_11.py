import spacy

# Matcherをインポート
from spacy.matcher import Matcher

nlp = spacy.load("ja_core_news_sm")
doc = nlp("AppleはiPhone Xの予約受付開始を発表しました。")

# 共有語彙データを用いてMatcherを初期化
matcher = Matcher(nlp.vocab)

# 「iPhone」と「X」にマッチするパターンを作成
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]

# matcherにパターンを追加
matcher.add("IPHONE_X_PATTERN", [pattern])

# docに対してmatcherを用いる
matches = matcher(doc)
print("Matches:", [doc[start:end].text for match_id, start, end in matches])
