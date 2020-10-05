import spacy

nlp = spacy.load("ja_core_news_sm")

text = "公式発表：Appleが米国の上場企業として初めて時価評価額1兆ドルに到達しました。"

# テキストを処理
doc = nlp(text)

# 予測された固有表現をイテレート
for ent in doc.ents:
    # 固有表現の文字列とラベルをプリント
    print(ent.text, ent.label_)
