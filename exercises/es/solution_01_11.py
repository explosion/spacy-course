import spacy

# Importa el Matcher
from spacy.matcher import Matcher

nlp = spacy.load("es_core_news_sm")
doc = nlp(
    "Los Olímpicos de Tokio 2020 son la inspiración para la nueva "
    "colección de zapatillas adidas ZX."
)

# Inicializa el matcher con el vocabulario compartido
matcher = Matcher(nlp.vocab)

# Crea un patrón que encuentre dos tokens: "adidas" y "ZX"
pattern = [{"TEXT": "adidas"}, {"TEXT": "ZX"}]

# Añade el patrón al matcher
matcher.add("ADIDAS_ZX_PATTERN", None, pattern)

# Usa al matcher sobre el doc
matches = matcher(doc)
print("Resultados:", [doc[start:end].text for match_id, start, end in matches])
