from spacy.lang.en import English
from spacy.tokens import Token

nlp = English()

# Déclare l'extension d'attribut de Token "is_country"
# avec la valeur par défaut False
____.____(____, ____=____)

# Traite le texte et définis l'attribut is_country à True pour le token "Spain"
doc = nlp("I live in Spain.")
____ = True

# Affiche le texte du token et l'attribut is_country pour tous les tokens
print([(____, ____) for token in doc])
