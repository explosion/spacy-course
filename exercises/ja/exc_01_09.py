import spacy

nlp = spacy.load("en_core_web_sm")

text = "Upcoming iPhone X release date leaked as Apple reveals pre-orders"

# テキストを処理
doc = ____

# 固有表現をイテレート
for ____ in ____.____:
    # 固有表現の文字列とラベルをプリント
    print(____.____, ____.____)

# iPhone Xのスパンを取得
iphone_x = ____

# スパンの文字列をプリント
print("Missing entity:", iphone_x.text)
