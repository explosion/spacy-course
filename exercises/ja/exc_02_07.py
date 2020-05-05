import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Berlin is a nice city")

# すべてのトークンの文字列と品詞タグを取得
token_texts = [token.text for token in doc]
pos_tags = [token.pos_ for token in doc]

for index, pos in enumerate(pos_tags):
    # 現在のトークンが固有名詞かどうかをチェック
    if pos == "PROPN":
        # 次のトークンが動詞かどうかをチェック
        if pos_tags[index + 1] == "VERB":
            result = token_texts[index]
            print("Found proper noun before a verb:", result)
