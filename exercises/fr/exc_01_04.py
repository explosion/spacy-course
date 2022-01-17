import spacy

nlp = spacy.blank("fr")

# Traite le texte
doc = nlp(
    "En 1990, plus de 60 % de la population d'Asie orientale vivait dans une pauvreté extrême. "
    "Actuellement c'est moins de 4 %."
)

# Itère sur les tokens du doc
for token in doc:
    # Vérifie si le token ressemble à un nombre
    if ____.____:
        # Obtiens le token suivant dans le document
        next_token = ____[____]
        # Vérifie si le texte du token suivant est égal à "%"
        if next_token.____ == "%":
            print("Pourcentage trouvé :", token.text)
