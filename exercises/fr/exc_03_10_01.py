import spacy
from spacy.tokens import Doc

nlp = spacy.blank("fr")

# Définis la fonction getter
def get_has_number(doc):
    # Retourne si un token quelconque du doc renvoie True pour token.like_num
    return any(____ for token in doc)


# Déclare l'extension de propriété de Doc "has_number"
# avec le getter get_has_number
____.____(____, ____=____)

# Traite le texte et vérifie l'attribut personnalisé has_number
doc = nlp("Le musée a fermé pour cinq ans en 2012.")
print("has_number :", ____)
