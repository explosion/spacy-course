import spacy

nlp = spacy.load("en_core_web_md")

doc1 = nlp("It's a warm summer day")
doc2 = nlp("It's sunny outside")

# doc1とdoc2の類似度を取得
similarity = doc1.similarity(doc2)
print(similarity)
