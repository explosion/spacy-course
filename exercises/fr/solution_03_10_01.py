import spacy
from spacy.tokens import Doc

nlp = spacy.blank("fr")

# Définis la fonction getter
def get_has_number(doc):
    # Retourne si un token quelconque du doc renvoie True pour token.like_num
    return any(token.like_num for token in doc)


# Déclare l'extension de propriété de Doc "has_number"
# avec le getter get_has_number
Doc.set_extension("has_number", getter=get_has_number)

# Traite le texte et vérifie l'attribut personnalisé has_number
doc = nlp("Le musée a fermé pour cinq ans en 2012.")
print("has_number :", doc._.has_number)
