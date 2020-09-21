import spacy

nlp = spacy.load("ja_core_news_md")

doc1 = nlp("暖かい夏の日です")
doc2 = nlp("外は晴れています")

# doc1とdoc2の類似度を取得
similarity = ____.____(____)
print(similarity)
