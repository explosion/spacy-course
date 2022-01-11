import spacy

nlp = spacy.load("fr_core_news_sm")
doc = nlp("Berlin semble être une jolie ville")

# Itère sur les tokens
for token in doc:
    # Vérifie si le token courant est un nom propre
    if token.pos_ == "PROPN":
        # Vérifie si le token suivant est un verbe
        if doc[token.i + 1].pos_ == "VERB":
            print("Trouvé un nom propre avant un verbe :", token.text)
