import spacy

nlp = spacy.load("ja_core_news_sm")

text = "静岡県にある三保の松原は世界遺産の一部です。"

# テキストを処理
doc = ____

# 固有表現をイテレート
for ____ in ____.____:
    # 固有表現の文字列とラベルをプリント
    print(____.____, ____.____)

# 三保の松原のスパンを取得
mihonomatsubara = ____

# スパンの文字列をプリント
print("Missing entity:", mihonomatsubara.text)
