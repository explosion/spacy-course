import spacy

# Importe le Matcher
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")

# Initialise le matcher avec le vocabulaire partagé
matcher = Matcher(nlp.vocab)

# Crée un motif qui recherche les deux tokens : "iPhone" et "X"
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]

# Ajoute le motif au matcher
matcher.add("IPHONE_X_PATTERN", None, pattern)

# Utilise le matcher sur le doc
matches = matcher(doc)
print("Résultats :", [doc[start:end].text for match_id, start, end in matches])
