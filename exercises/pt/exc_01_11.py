import spacy

# Importe o comparador - Matcher
from spacy.____ import ____

nlp = spacy.load("pt_core_news_sm")
doc = nlp("Vazou a data de lançamento do novo iPhone X após a Apple revelar a existência de compras antecipadas.")

# Inicialize o comparador com o vocabulário compartilhado 
matcher = ____(____.____)

# Crie uma expressão que faça a correspondência dos tokens: "iPhone" and "X"
pattern = [____]

# Adicione uma expressão ao comparador
____.____("IPHONE_X_PATTERN", ____)

# Use o comparador no doc
matches = ____
print("Correspondências:", [doc[start:end].text for match_id, start, end in matches])
