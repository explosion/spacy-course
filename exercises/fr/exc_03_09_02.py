from spacy.lang.en import English
from spacy.tokens import Token

nlp = English()

# Définis la fonction getter qui prend en argument un token et retourne son texte inversé
def get_reversed(token):
    return token.text[::-1]


# Déclare l'extension de propriété de Token "reversed" avec le getter get_reversed
____.____(____, ____=____)

# Traite le texte et affiche l'attribut inversé pour chaque token
doc = nlp("All generalizations are false, including this one.")
for ____ in ____:
    print("reversed:", ____)
