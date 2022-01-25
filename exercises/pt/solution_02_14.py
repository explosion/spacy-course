import json
import spacy

with open("exercises/pt/countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())

nlp = spacy.blank("pt")
doc = nlp("A República Tcheca deve ajudar a Eslováquia a proteger seu espaço aéreo.")

# Importar o PhraseMatcher e inicializá-lo
from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

# Criar objeto com a expressão e adicioná-lo ao comparador matcher
# Essa é a forma mais eficiente: [nlp(country) for country in COUNTRIES]
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", patterns)

# Chamar o matcher no documento de teste e imprimir o resultado
matches = matcher(doc)
print([doc[start:end] for match_id, start, end in matches])
