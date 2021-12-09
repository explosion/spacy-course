import spacy

nlp = spacy.blank("ja")

# Docクラスをインポート
from ____ import ____

# 作りたいテキスト：「さあ、始めよう！」
words = ["さあ", "、", "初めよう", "！"]
spaces = [____, ____, ____, ____]

# wordsとspacesからDocを作成
doc = ____(____, ____=____, ____=____)
print(doc.text)
