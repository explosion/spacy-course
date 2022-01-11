import spacy

# Importe le Matcher
from spacy.____ import ____

nlp = spacy.load("fr_core_news_sm")
doc = nlp("Apple : le nouveau modèle X Pro attendu pour l'été.")

# Initialise le matcher avec le vocabulaire partagé
matcher = ____(____.____)

# Crée un motif qui recherche les deux tokens : "X" et "Pro"
pattern = [____]

# Ajoute le motif au matcher
____.____("IPHONE_X_PATTERN", ____)

# Utilise le matcher sur le doc
matches = ____
print("Résultats :", [doc[start:end].text for match_id, start, end in matches])
