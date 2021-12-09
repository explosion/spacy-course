import spacy

nlp = spacy.blank("ja")

# テキストを処理
doc = nlp(
    "1990年には東アジアの60%以上の人々が極度の貧困状態に陥っていました。"
    "今では4%以下になっています。"
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
