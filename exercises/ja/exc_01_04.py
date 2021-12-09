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
    if ____.____:
        # docの次のトークンを取得
        next_token = ____[____]
        # 次のトークンの文字列が「%」に一致するかどうかをチェック
        if next_token.____ == "%":
            print("Percentage found:", token.text)
