import spacy

# Importe le Matcher
from spacy.matcher import Matcher

nlp = spacy.load("fr_core_news_sm")
doc = nlp("Le constructeur Citröen présente la e-Méhari Courrèges au public.")

# Initialise le matcher avec le vocabulaire partagé
matcher = Matcher(nlp.vocab)

# Crée un motif qui recherche les deux tokens : "e-Méhari" et "Courrèges"
pattern = [{"TEXT": "e-Méhari"}, {"TEXT": "Courrèges"}]

# Ajoute le motif au matcher
matcher.add("MEHARI_PATTERN", None, pattern)

# Utilise le matcher sur le doc
matches = matcher(doc)
print("Résultats :", [doc[start:end].text for match_id, start, end in matches])
