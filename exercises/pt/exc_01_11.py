import spacy

# Importe o comparador - Matcher
from spacy.____ import ____

nlp = spacy.load("en_core_web_sm")
doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")

# Inicialize o comparador com o vocabulário compartilhado 
matcher = ____(____.____)

# Crie uma expressão que faça a correspondência dos tokens: "iPhone" and "X"
pattern = [____]

# Adicione uma expressão ao comparador
____.____("IPHONE_X_PATTERN", None, ____)

# Use o comparador no doc
matches = ____
print("Matches:", [doc[start:end].text for match_id, start, end in matches])
