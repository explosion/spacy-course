from spacy.lang.en import English

nlp = English()

# テキストを処理
doc = nlp(
    "In 1990, more than 60% of people in East Asia were in extreme poverty. "
    "Now less than 4% are."
)

# docに含まれるトークンを処理
for token in doc:
    # トークンが数字に似ているかどうかをチェック
    if token.like_num:
        # docの次のトークンを取得
        next_token = doc[token.i + 1]
        # 次のトークンの文字列が「%」に一致するかどうかをチェック
        if next_token.text == "%":
            print("Percentage found:", token.text)
