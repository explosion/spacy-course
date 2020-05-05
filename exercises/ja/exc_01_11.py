import spacy

# Matcherをインポート
from spacy.____ import ____

nlp = spacy.load("en_core_web_sm")
doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")

# 共有語彙データを用いてMatcherを初期化
matcher = ____(____.____)

# 「iPhone」と「X」にマッチするパターンを作成
pattern = [____]

# matcherにパターンを追加
____.____("IPHONE_X_PATTERN", None, ____)

# docに対してmatcherを用いる
matches = ____
print("Matches:", [doc[start:end].text for match_id, start, end in matches])
