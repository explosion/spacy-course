# Importe la classe de langue "German"
from spacy.lang.de import German

# Crée l'objet nlp
nlp = German()

# Traite un texte (il signifie "Cordiales salutations !" en allemand)
doc = nlp("Liebe Grüße!")

# Affiche le texte du document
print(doc.text)
