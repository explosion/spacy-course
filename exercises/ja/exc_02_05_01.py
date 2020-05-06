from spacy.lang.en import English

nlp = English()

# Docクラスをインポート
from ____ import ____

# 作りたいテキスト：「spaCy is cool!」
words = ["spaCy", "is", "cool", "!"]
spaces = [True, True, False, False]

# wordsとspacesからDocを作成
doc = ____(____, words=words, spaces=spaces)
print(doc.text)
