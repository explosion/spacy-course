import spacy
from spacy.tokens import Token

nlp = spacy.blank("fr")

# Définis la fonction getter qui prend en argument un token
# et retourne son texte inversé
def get_reversed(token):
    return token.text[::-1]


# Déclare l'extension de propriété de Token "reversed"
# avec le getter get_reversed
Token.set_extension("reversed", getter=get_reversed)

# Traite le texte et affiche l'attribut inversé pour chaque token
doc = nlp("Toutes les généralisations sont fausses, celle-ci aussi.")
for token in doc:
    print("reversed :", token._.reversed)
