import spacy

# Importe o comparador - Matcher
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")

# Inicialize o comparador com o vocabulário compartilhado 
matcher = Matcher(nlp.vocab)

# Crie um padrão que faça a correspondência dos tokens: "iPhone" and "X"
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]

# Adicione esse padrão ao comparador
matcher.add("IPHONE_X_PATTERN", None, pattern)

# Use o comparador no doc
matches = matcher(doc)
print("Matches:", [doc[start:end].text for match_id, start, end in matches])
