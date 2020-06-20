import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Berlin is a nice city")

# Itère sur les tokens
for token in doc:
    # Vérifie si le token courant est un nom propre
    if token.pos_ == "PROPN":
        # Vérifie si le token suivant est un verbe
        if doc[token.i + 1].pos_ == "VERB":
            print("Found proper noun before a verb:", token.text)
