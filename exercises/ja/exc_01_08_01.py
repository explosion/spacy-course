import spacy

nlp = spacy.load("ja_core_news_sm")

text = "公式発表：Appleが米国の上場企業として初めて時価評価額1兆ドルに到達しました。"

# テキストを処理
doc = ____

for token in doc:
    # トークンの文字列、品詞タグ、依存関係ラベルを取得
    token_text = ____.____
    token_pos = ____.____
    token_dep = ____.____
    # フォーマットしてプリント
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")
