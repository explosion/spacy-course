import spacy

nlp = spacy.load("en_core_web_sm")

text = "Upcoming iPhone X release date leaked as Apple reveals pre-orders"

# テキストを処理
doc = nlp(text)

# 固有表現をイテレート
for ent in doc.ents:
    # 固有表現の文字列とラベルをプリント
    print(ent.text, ent.label_)

# iPhone Xのスパンを取得
iphone_x = doc[1:3]

# スパンの文字列をプリント
print("Missing entity:", iphone_x.text)
