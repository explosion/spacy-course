import spacy

nlp = spacy.load("es_core_news_sm")
doc = nlp("Por Berlín fluye el río Esprea.")

# Obtén todos los tokens y los part-of-speech tags
token_texts = [token.text for token in doc]
pos_tags = [token.pos_ for token in doc]

for index, pos in enumerate(pos_tags):
    # Revisa si el token actual es un nombre propio
    if pos == "PROPN":
        # Revisa si el siguiente token es un verbo
        if pos_tags[index + 1] == "VERB":
            result = token_texts[index]
            print("Encontré un nombre propio antes de un verbo:", result)
