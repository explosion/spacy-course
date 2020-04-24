import json
from spacy.lang.en import English

with open("exercises/en/countries.json") as f:
    COUNTRIES = json.loads(f.read())

nlp = English()
doc = nlp("Czech Republic may help Slovakia protect its airspace")

# Importa el PhraseMatcher e inicialízalo
from spacy.____ import ____

matcher = ____(____)

# Crea objetos Doc patrón y añádelos al matcher
# Esta es una versión más rápida de: [nlp(country) for country in COUNTRIES]
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", None, *patterns)

# Llama al matcher sobre el documento de prueba e imprime el resultado en pantalla
matches = ____(____)
print([doc[start:end] for match_id, start, end in matches])
