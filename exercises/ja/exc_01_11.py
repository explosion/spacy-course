import spacy

# Matcherをインポート
from spacy.____ import ____

nlp = spacy.load("ja_core_news_sm")
doc = nlp("AppleはiPhone Xの予約受付開始を発表しました。")

# 共有語彙データを用いてMatcherを初期化
matcher = ____(____.____)

# 「iPhone」と「X」にマッチするパターンを作成
pattern = [____]

# matcherにパターンを追加
____.____("IPHONE_X_PATTERN", ____)

# docに対してmatcherを用いる
matches = ____
print("Matches:", [doc[start:end].text for match_id, start, end in matches])
