import spacy

# Importa el Matcher
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
doc = nlp("New iPhone X release date leaked as Apple reveals pre-orders by mistake")

# Inicializa el matcher con el vocabulario compartido
matcher = Matcher(nlp.vocab)

# Crea un patrón que encuentre dos tokens: "iPhone" y "X"
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]

# Añade el patrón al matcher
matcher.add("IPHONE_X_PATTERN", None, pattern)

# Usa al matcher sobre el doc
matches = matcher(doc)
print("Matches:", [doc[start:end].text for match_id, start, end in matches])
