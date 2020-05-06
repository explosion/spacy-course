import spacy

nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# テキストを処理
doc = nlp(text)

for token in doc:
    # トークンの文字列、品詞タグ、依存関係ラベルを取得
    token_text = token.text
    token_pos = token.pos_
    token_dep = token.dep_
    # フォーマットしてプリント
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")
