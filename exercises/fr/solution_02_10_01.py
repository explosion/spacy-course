import spacy

nlp = spacy.load("fr_core_news_md")

doc1 = nlp("Le temps est au beau fixe")
doc2 = nlp("Le ciel est clair")

# Obtiens la similarité entre doc1 et doc2
similarity = doc1.similarity(doc2)
print(similarity)
