import spacy

nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# テキストを処理
doc = ____

for token in doc:
    # トークンの文字列、品詞タグ、依存関係ラベルを取得
    token_text = ____.____
    token_pos = ____.____
    token_dep = ____.____
    # フォーマットしてプリント
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")
