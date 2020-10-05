import spacy

nlp = spacy.load("ja_core_news_md")

doc = nlp("テレビと本")
token1, token2 = doc[0], doc[2]

# 「テレビ」と「本」の類似度を取得
similarity = ____.____(____)
print(similarity)
