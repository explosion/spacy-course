import spacy

nlp = spacy.load("ja_core_news_sm")

text = "宮城県にある松島は日本三景の一つです。"

# テキストを処理
doc = ____

# 固有表現をイテレート
for ____ in ____.____:
    # 固有表現の文字列とラベルをプリント
    print(____.____, ____.____)

# 松島のスパンを取得
matsushima = ____

# スパンの文字列をプリント
print("Missing entity:", matsushima.text)
