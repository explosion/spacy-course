from spacy.lang.en import English

nlp = English()

# Docクラスをインポート
from spacy.tokens import Doc

# 作成したいテキスト：「Oh, really?!」
words = ["Oh", ",", "really", "?", "!"]
spaces = [False, True, False, False, False]

# Docをwordsとspacesから作成
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
