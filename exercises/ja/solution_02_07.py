import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Berlin looks like a nice city")

# すべてのトークンの文字列と品詞タグを取得
for token in doc:
    # 現在のトークンが固有名詞かどうかをチェック
    if token.pos_ == "PROPN":
        # 次のトークンが動詞かどうかをチェック
        if doc[token.i + 1].pos_ == "VERB":
            print("Found proper noun before a verb:", token.text)
