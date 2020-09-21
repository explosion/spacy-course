from spacy.lang.ja import Japanese

nlp = Japanese()

# DocとSpanクラスをインポート
from spacy.tokens import Doc, Span

words = ["私", "は", "デヴィッド", "・", "ボウイ", "が", "好き"]
spaces = [False, False, False, False, False, False, False]

# docをwordsとspacesから作成
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

# docから「デヴィッド・ボウイ」というスパンを作成し、「PERSON」ラベルを付ける
span = Span(doc, 2, 5, label="PERSON")
print(span.text, span.label_)

# docの固有表現リストにspanを追加
doc.ents = [span]

# 固有表現の文字列とラベルをプリント
print([(ent.text, ent.label_) for ent in doc.ents])
