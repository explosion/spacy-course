# Importe spaCy
import spacy

# Crée l'objet nlp français
nlp = spacy.blank("fr")

# Traite un texte
doc = nlp("Ceci est une phrase.")

# Affiche le texte du document
print(doc.text)
