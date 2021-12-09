import json
import spacy

with open("exercises/de/countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())

nlp = spacy.blank("de")
doc = nlp("Tschechien könnte der Slowakei dabei helfen, ihren Luftraum zu schützen")

# Importiere den PhraseMatcher und initialisiere ihn
from spacy.____ import ____

matcher = ____(____)

# Erstelle Pattern-Doc-Objekte und füge sie zum Matcher hinzu
# Dies ist die schnellere Version von: [nlp(country) for country in COUNTRIES]
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", patterns)

# Wende den Matcher auf das Test-Dokument an und drucke das Resultat
matches = ____(____)
print([doc[start:end] for match_id, start, end in matches])
