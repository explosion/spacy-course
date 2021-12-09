import spacy

# Importa el Matcher
from spacy.matcher import Matcher

nlp = spacy.load("es_core_news_sm")
doc = nlp(
    "Los Olímpicos de Tokio 2020 son la inspiración para la nueva "
    "colección de zapatillas adidas zx."
)

# Inicializa el matcher con el vocabulario compartido
matcher = Matcher(nlp.vocab)

# Crea un patrón que encuentre dos tokens: "adidas" y "zx"
pattern = [{"TEXT": "adidas"}, {"TEXT": "zx"}]

# Añade el patrón al matcher
matcher.add("ADIDAS_ZX_PATTERN", [pattern])

# Usa al matcher sobre el doc
matches = matcher(doc)
print("Resultados:", [doc[start:end].text for match_id, start, end in matches])
