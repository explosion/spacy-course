import spacy

nlp = spacy.load("ja_core_news_sm")

text = "静岡県にある三保の松原は世界遺産の一部です。"

# テキストを処理
doc = nlp(text)

# 固有表現をイテレート
for ent in doc.ents:
    # 固有表現の文字列とラベルをプリント
    print(ent.text, ent.label_)

# 三保の松原のスパンを取得
mihonomatsubara = doc[4:7]

# スパンの文字列をプリント
print("Missing entity:", mihonomatsubara.text)