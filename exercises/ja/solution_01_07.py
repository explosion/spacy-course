import spacy

# 「en_core_web_sm」モデルをロード
nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# テキストを処理
doc = nlp(text)

# docのテキストをプリント
print(doc.text)
