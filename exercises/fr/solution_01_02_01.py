# Importe la classe de langue "English"
from spacy.lang.en import English

# Crée l'objet nlp
nlp = English()

# Traite un texte
doc = nlp("This is a sentence.")

# Affiche le texte du document
print(doc.text)
