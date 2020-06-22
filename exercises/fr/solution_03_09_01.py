from spacy.lang.en import English
from spacy.tokens import Token

nlp = English()

# Déclare l'extension d'attribut de Token "is_country" avec la valeur par défaut False
Token.set_extension("is_country", default=False)

# Traite le texte et définis l'attribut is_country à True pour le token "Spain"
doc = nlp("I live in Spain.")
doc[3]._.is_country = True

# Affiche le texte du token et l'attribut is_country pour tous les tokens
print([(token.text, token._.is_country) for token in doc])
