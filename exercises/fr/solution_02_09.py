import spacy

# Charge le pipeline fr_core_news_md
nlp = spacy.load("fr_core_news_md")

# Traite le texte
doc = nlp("Deux bananes en pyjamas")

# Obtiens le vecteur pour le token "bananes"
bananas_vector = doc[1].vector
print(bananas_vector)
