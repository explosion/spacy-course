# Importe la classe de langue "Français" et crée l'objet nlp
from spacy.lang.fr import French

nlp = French()

# Traite le texte
doc = nlp("La forêt est peuplée de loups gris et renards roux.")

# Sélectionne le premier token
first_token = doc[0]

# Affiche le texte du premier token
print(first_token.text)
