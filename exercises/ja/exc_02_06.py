from spacy.lang.ja import Japanese

nlp = Japanese()

# DocとSpanクラスをインポート
from spacy.____ import ____, ____

words = ["私", "は", "デヴィッド", "・", "ボウイ", "が", "好き"]
spaces = [False, False, False, False, False, False, False]

# docをwordsとspacesから作成
doc = ____(____, ____, ____)
print(doc.text)

# docから「デヴィッド・ボウイ」というスパンを作成し、「PERSON」ラベルを付ける
span = ____(____, ____, ____, label=____)
print(span.text, span.label_)

# docの固有表現リストにspanを追加
____.____ = [____]

# 固有表現の文字列とラベルをプリント
print([(ent.text, ent.label_) for ent in doc.ents])
