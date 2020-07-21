from spacy.lang.fr import French
from spacy.tokens import Token

nlp = French()

# Déclare l'extension d'attribut de Token "is_country"
# avec la valeur par défaut False
____.____(____, ____=____)

# Traite le texte et définis l'attribut is_country à True pour le token "Suisse"
doc = nlp("J'habite en Suisse.")
____ = True

# Affiche le texte du token et l'attribut is_country pour tous les tokens
print([(____, ____) for token in doc])
