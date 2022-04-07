import spacy

# Importe o comparador - Matcher
from spacy.matcher import Matcher

nlp = spacy.load("pt_core_news_sm")
doc = nlp("Vazou a data de lançamento do novo iPhone X após a Apple revelar a existência de compras antecipadas.")

# Inicialize o comparador com o vocabulário compartilhado 
matcher = Matcher(nlp.vocab)

# Crie uma expressão que faça a correspondência dos tokens: "iPhone" and "X"
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]

# Adicione uma expressão ao comparador
matcher.add("IPHONE_X_PATTERN", [pattern])

# Use o comparador no doc
matches = matcher(doc)
print("Correspondências:", [doc[start:end].text for match_id, start, end in matches])