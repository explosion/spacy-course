import spacy

nlp = spacy.load("ja_core_news_sm")
doc = nlp("ベルリンはいい街だと思う")

# すべてのトークンの文字列と品詞タグを取得
for token in doc:
    # 現在のトークンが固有名詞かどうかをチェック
    if token.pos_ == "PROPN":
        # 次のトークンが設置詞かどうかをチェック
        if doc[token.i + 1].pos_ == "ADP":
            print("設置詞の前の固有名詞が見つかりました:", token.text)
