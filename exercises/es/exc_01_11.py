import spacy

# Importa el Matcher
from spacy.____ import ____

nlp = spacy.load("es_core_news_sm")
doc = nlp(
    "Los Olímpicos de Tokio 2020 son la inspiración para la nueva "
    "colección de zapatillas adidas pro."
)

# Inicializa el matcher con el vocabulario compartido
matcher = ____(____.____)

# Crea un patrón que encuentre dos tokens: "adidas" y "pro"
pattern = [____]

# Añade el patrón al matcher
____.____("ADIDAS_PRO_PATTERN", None, ____)

# Usa al matcher sobre el doc
matches = ____
print("Resultados:", [doc[start:end].text for match_id, start, end in matches])
