from spacy.lang.ja import Japanese

nlp = Japanese()

# Docクラスをインポート
from spacy.tokens import Doc

# 作りたいテキスト：「さあ、始めよう！」
words = ["さあ", "、", "始めよう", "！"]
spaces = [False, False, False, False]

# wordsとspacesからDocを作成
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
