from spacy.lang.ja import Japanese

nlp = Japanese()

# Docクラスをインポート
from spacy.tokens import Doc

# 作りたいテキスト：「spaCyは素晴らしい！」
words = ["spaCy", "は", "素晴らしい", "！"]
spaces = [False, False, False, False]

# wordsとspacesからDocを作成
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
