# Importe la classe de langue "English" et crée l'objet nlp
from spacy.lang.en import English

nlp = English()

# Traite le texte
doc = nlp("I like tree kangaroos and narwhals.")

# Sélectionne le premier token
first_token = doc[0]

# Affiche le texte du premier token
print(first_token.text)
