from spacy.lang.en import English

nlp = English()

# DocとSpanクラスをインポート
from spacy.____ import ____, ____

words = ["I", "like", "David", "Bowie"]
spaces = [True, True, True, False]

# docをwordsとspacesから作成
doc = ____(____, ____, ____)
print(doc.text)

# docから「David Bowie」というスパンを作成し、「PERSON」ラベルを付ける
span = ____(____, ____, ____, label=____)
print(span.text, span.label_)

# docの固有表現リストにspanを追加
____.____ = [____]

# 固有表現の文字列とラベルをプリント
print([(ent.text, ent.label_) for ent in doc.ents])
