import json
from spacy.lang.es import Spanish

with open("exercises/es/countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())

nlp = Spanish()
doc = nlp(
    "La Unión Europea fue fundada por seis países de Europa occidental "
    "(Francia, Alemania, Italia, Bélgica, Países Bajos, y Luxemburgo) y "
    "se amplió en seis ocasiones."
)

# Importa el PhraseMatcher e inicialízalo
from spacy.____ import ____

matcher = ____(____)

# Crea objetos Doc patrón y añádelos al matcher
# Esta es una versión más rápida de: [nlp(country) for country in COUNTRIES]
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", None, *patterns)

# Llama al matcher sobre el documento de prueba e imprime el 
# resultado en pantalla
matches = ____(____)
print([doc[start:end] for match_id, start, end in matches])
