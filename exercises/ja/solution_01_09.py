import spacy

nlp = spacy.load("ja_core_news_sm")

text = "宮城県にある松島は日本三景の一つです。"

# テキストを処理
doc = nlp(text)

# 固有表現をイテレート
for ent in doc.ents:
    # 固有表現の文字列とラベルをプリント
    print(ent.text, ent.label_)

# 松島のスパンを取得
matsushima = doc[4:5]

# スパンの文字列をプリント
print("Missing entity:", matsushima.text)
