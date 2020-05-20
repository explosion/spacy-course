import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Berlin is a nice city")

# Itera sobre los tokens
for token in doc:
    # Revisa si el token actual es un nombre propio
    if token.pos_ == "PROPN":
        # Revisa si el siguiente token es un verbo
        if doc[token.i + 1].pos_ == "VERB":
            print("Found proper noun before a verb:", token.text)
