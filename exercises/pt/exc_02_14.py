import json
import spacy

with open("exercises/en/countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())

nlp = spacy.blank("en")
doc = nlp("Czech Republic may help Slovakia protect its airspace")

# Importar o PhraseMatcher e inicializá-lo
from spacy.____ import ____

matcher = ____(____)

# Criar objeto com a expressão e adicioná-lo ao comparador matcher
# Essa é a forma mais eficiente: [nlp(country) for country in COUNTRIES]
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", patterns)

# Chamar o matcher no documento de teste e imprimir o resultado
matches = ____(____)
print([doc[start:end] for match_id, start, end in matches])
