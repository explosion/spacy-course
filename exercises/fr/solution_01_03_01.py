# Importe spacy et crée l'objet nlp français
import spacy

nlp = spacy.blank("fr")

# Traite le texte
doc = nlp("La forêt est peuplée de loups gris et renards roux.")

# Sélectionne le premier token
first_token = doc[0]

# Affiche le texte du premier token
print(first_token.text)
