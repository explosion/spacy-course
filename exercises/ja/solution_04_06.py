import spacy

# 空の「ja」モデルを作成
nlp = spacy.blank("ja")

# 新しい固有表現抽出器を作成し、パイプラインに追加
ner = nlp.add_pipe("ner")

# 「GADGET」ラベルを固有表現抽出器に追加
ner.add_label("GADGET")
