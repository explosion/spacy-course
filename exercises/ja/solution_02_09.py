import spacy

# en_core_web_mdモデルをロード
nlp = spacy.load("en_core_web_md")

# テキストを処理
doc = nlp("Two bananas in pyjamas")

# 「bananas」のベクトルを取得
bananas_vector = doc[1].vector
print(bananas_vector)
