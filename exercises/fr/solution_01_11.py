import spacy

# Importe le Matcher
from spacy.matcher import Matcher

nlp = spacy.load("fr_core_news_sm")
doc = nlp("Apple : le nouveau modèle X Pro attendu pour l'été.")

# Initialise le matcher avec le vocabulaire partagé
matcher = Matcher(nlp.vocab)

# Crée un motif qui recherche les deux tokens : "X" et "Pro"
pattern = [{"TEXT": "X"}, {"TEXT": "Pro"}]

# Ajoute le motif au matcher
matcher.add("IPHONE_X_PATTERN", [pattern])

# Utilise le matcher sur le doc
matches = matcher(doc)
print("Résultats :", [doc[start:end].text for match_id, start, end in matches])
