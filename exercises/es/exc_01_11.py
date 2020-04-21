import spacy

# Importa el Matcher
from spacy.____ import ____

nlp = spacy.load("en_core_web_sm")
doc = nlp("New iPhone X release date leaked as Apple reveals pre-orders by mistake")

# Inicializa el matcher con el vocabulario compartido
matcher = ____(____.____)

# Crea un patrpon que encuentre dos tokens: "iPhone" y "X"
pattern = [____]

# Añade el patrón al matcher
____.____("IPHONE_X_PATTERN", None, ____)

# Usa al matcher sobre el doc
matches = ____
print("Matches:", [doc[start:end].text for match_id, start, end in matches])
