import json
from spacy.lang.de import German

with open("exercises/de/countries.json") as f:
    COUNTRIES = json.loads(f.read())

nlp = German()
doc = nlp("Tschechien könnte der Slowakei dabei helfen, ihren Luftraum zu schützen")

# Importiere den PhraseMatcher und initialisiere ihn
from spacy.____ import ____

matcher = ____(____)

# Erstelle Pattern-Doc-Objekte und füge sie zum Matcher hinzu
# Dies ist die schnellere Version von: [nlp(country) for country in COUNTRIES]
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", None, *patterns)

# Wende den Matcher auf das Test-Dokument an und drucke das Resultat
matches = ____(____)
print([doc[start:end] for match_id, start, end in matches])
