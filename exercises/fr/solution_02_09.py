import spacy

# Charge le modèle en_core_web_md
nlp = spacy.load("en_core_web_md")

# Traite le texte
doc = nlp("Two bananas in pyjamas")

# Obtiens le vecteur pour le token "bananas"
bananas_vector = doc[1].vector
print(bananas_vector)
