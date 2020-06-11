import spacy

# Importe le Matcher
from spacy.____ import ____

nlp = spacy.load("en_core_web_sm")
doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")

# Initialise le matcher avec le vocabulaire partagé
matcher = ____(____.____)

# Crée un motif qui recherche les deux tokens : "iPhone" et "X"
pattern = [____]

# Ajoute le motif au matcher
____.____("IPHONE_X_PATTERN", None, ____)

# Utilise le matcher sur le doc
matches = ____
print("Résultats :", [doc[start:end].text for match_id, start, end in matches])
