# Importe spaCy
import spacy

# Crée l'objet nlp espagnol
nlp = spacy.blank("es")

# Traite un texte (il signifie "Comment vas-tu ?" en espagnol)
doc = nlp("¿Cómo estás?")

# Affiche le texte du document
print(doc.text)
