import json
from spacy.lang.en import English

with open("exercises/en/countries.json") as f:
    COUNTRIES = json.loads(f.read())

nlp = English()
doc = nlp("Czech Republic may help Slovakia protect its airspace")

# Importe le PhraseMatcher et initialise-le
from spacy.____ import ____

matcher = ____(____)

# Crée des motifs objets Doc et ajoute-les au matcher
# C'est la version rapide de : [nlp(country) for country in COUNTRIES]
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", None, *patterns)

# Appelle le matcher sur le document de test et affiche le résultat
matches = ____(____)
print([doc[start:end] for match_id, start, end in matches])
