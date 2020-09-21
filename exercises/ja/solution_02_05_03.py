from spacy.lang.ja import Japanese

nlp = Japanese()

# Docクラスをインポート
from spacy.tokens import Doc

# 作成したいテキスト：「本当ですか？！」
words = ["本当", "です", "か", "？", "！"]
spaces = [False, False, False, False, False]

# Docをwordsとspacesから作成
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
