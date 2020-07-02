# Importe la classe de langue "French"
from spacy.lang.fr import French

# Crée l'objet nlp
nlp = French()

# Traite un texte
doc = nlp("Ceci est une phrase.")

# Affiche le texte du document
print(doc.text)
