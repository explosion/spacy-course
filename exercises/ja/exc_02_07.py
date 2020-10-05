import spacy

nlp = spacy.load("ja_core_news_sm")
doc = nlp("ベルリンはいい街だと思う")

# すべてのトークンの文字列と品詞タグを取得
token_texts = [token.text for token in doc]
pos_tags = [token.pos_ for token in doc]

for index, pos in enumerate(pos_tags):
    # 現在のトークンが固有名詞かどうかをチェック
    if pos == "PROPN":
        # 次のトークンが接置詞かどうかをチェック
        if pos_tags[index + 1] == "ADP":
            result = token_texts[index]
            print("接置詞の前の固有名詞が見つかりました:", result)
