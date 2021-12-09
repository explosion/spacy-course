import spacy

nlp = spacy.load("en_core_web_md")

doc1 = nlp("It's a warm summer day")
doc2 = nlp("It's sunny outside")

# Obtenha a similiridade entre doc1 e doc2
similarity = doc1.similarity(doc2)
print(similarity)
