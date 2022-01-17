# Importe spaCy
import spacy

# Crée l'objet nlp anglais
nlp = spacy.blank("en")

# Traite un texte (il signifie "Ceci est une phrase" en anglais)
doc = nlp("This is a sentence.")

# Affiche le texte du document
print(doc.text)
