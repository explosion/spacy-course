# Importe la classe de langue "Spanish"
from spacy.lang.es import Spanish

# Crée l'objet nlp
nlp = Spanish()

# Traite un texte (il signifie "Comment vas-tu ?" en espagnol)
doc = nlp("¿Cómo estás?")

# Affiche le texte du document
print(doc.text)
