import spacy

nlp = spacy.load("es_core_news_sm")
doc = nlp("Por Berlín fluye el río Esprea.")

# Itera sobre los tokens
for token in doc:
    # Revisa si el token actual es un nombre propio
    if token.pos_ == "PROPN":
        # Revisa si el siguiente token es un verbo
        if doc[token.i + 1].pos_ == "VERB":
            print("Encontré un nombre propio antes de un verbo:", token.text)
