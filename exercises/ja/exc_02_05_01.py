from spacy.lang.ja import Japanese

nlp = Japanese()

# Docクラスをインポート
from ____ import ____

# 作りたいテキスト：「spaCyは素晴らしい！」
words = ["spaCy", "は", "素晴らしい", "！"]
spaces = [False, False, False, False]

# wordsとspacesからDocを作成
doc = ____(____, words=words, spaces=spaces)
print(doc.text)
