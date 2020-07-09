import spacy

nlp = spacy.load("fr_core_news_md")

doc = nlp("C'était un super restaurant. Ensuite nous sommes allés dans un bar vraiment sympa.")

# Crée des spans pour "super restaurant" et "bar vraiment sympa"
span1 = ____
span2 = ____

# Obtiens la similarité entre les spans
similarity = ____.____(____)
print(similarity)
