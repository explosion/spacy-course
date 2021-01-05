import spacy

# ja_core_news_mdモデルをロード
nlp = spacy.load("ja_core_news_md")

# テキストを処理
doc = nlp("パジャマを着た2つのバナナ")

# 「バナナ」のベクトルを取得
bananas_vector = doc[7].vector
print(bananas_vector)
