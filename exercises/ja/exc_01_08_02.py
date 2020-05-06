import spacy

nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# テキストを処理
doc = ____

# 予測された固有表現をイテレート
for ent in ____.____:
    # 固有表現の文字列とラベルをプリント
    print(ent.____, ____.____)
