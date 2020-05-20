from spacy.lang.en import English

nlp = English()

# Docクラスをインポート
from spacy.tokens import Doc

# 作りたいテキスト：「Go, get started!」
words = ["Go", ",", "get", "started", "!"]
spaces = [False, True, True, False, False]

# wordsとspacesからDocを作成
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
