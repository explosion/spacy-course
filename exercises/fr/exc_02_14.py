import json
import spacy

with open("exercises/fr/countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())

nlp = spacy.blank("fr")
doc = nlp("La Tchéquie pourrait aider la Slovaquie à protéger son espace aérien")

# Importe le PhraseMatcher et initialise-le
from spacy.____ import ____

matcher = ____(____)

# Crée des motifs objets Doc et ajoute-les au matcher
# C'est la version rapide de : [nlp(country) for country in COUNTRIES]
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", patterns)

# Appelle le matcher sur le document de test et affiche le résultat
matches = ____(____)
print([doc[start:end] for match_id, start, end in matches])
