import spacy

# 「ja_core_news_sm」パイプラインをロード
nlp = spacy.load("ja_core_news_sm")

text = "公式発表：Appleが米国の上場企業として初めて時価評価額1兆ドルに到達しました。"

# テキストを処理
doc = nlp(text)

# docのテキストをプリント
print(doc.text)
