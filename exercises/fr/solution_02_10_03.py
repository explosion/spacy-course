import spacy

nlp = spacy.load("fr_core_news_md")

doc = nlp("C'était un super restaurant. Ensuite nous sommes allés dans un bar vraiment sympa.")

# Crée des spans pour "super restaurant" et "bar vraiment sympa"
span1 = doc[3:5]
span2 = doc[12:15]

# Obtiens la similarité entre les spans
similarity = span1.similarity(span2)
print(similarity)
