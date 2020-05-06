from spacy.lang.en import English

nlp = English()

# DocとSpanクラスをインポート
from spacy.tokens import Doc, Span

words = ["I", "like", "David", "Bowie"]
spaces = [True, True, True, False]

# docをwordsとspacesから作成
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

# docから「David Bowie」というスパンを作成し、「PERSON」ラベルを付ける
span = Span(doc, 2, 4, label="PERSON")
print(span.text, span.label_)

# docの固有表現リストにspanを追加
doc.ents = [span]

# 固有表現の文字列とラベルをプリント
print([(ent.text, ent.label_) for ent in doc.ents])
