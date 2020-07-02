from spacy.lang.en import English

nlp = English()

# Traite le texte
doc = nlp(
    "In 1990, more than 60% of people in East Asia were in extreme poverty. "
    "Now less than 4% are."
)

# Itère sur les tokens du doc
for token in doc:
    # Vérifie si le token ressemble à un nombre
    if token.like_num:
        # Obtiens le token suivant dans le document
        next_token = doc[token.i + 1]
        # Vérifie si le texte du token suivant est égal à "%"
        if next_token.text == "%":
            print("Percentage found:", token.text)
