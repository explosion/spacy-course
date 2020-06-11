import spacy
from spacy.matcher import Matcher

nlp = spacy.load("es_core_news_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "El gigante tecnológico IBM está ofreciendo lecciones virtuales "
    "sobre tecnologías avanzadas gratuitas en español."
)

# Escribe un patrón para un sustantivo más uno o dos adjetivos
pattern = [{"POS": "NOUN"}, {"POS": "ADJ"}, {"POS": "ADJ", "OP": "?"}]

# Añade el patrón al matcher y usa el matcher sobre el documento
matcher.add("NOUN_ADJ_PATTERN", None, pattern)
matches = matcher(doc)
print("Total de resultados encontrados:", len(matches))

# Itera sobre los resultados e imprime el texto del span
for match_id, start, end in matches:
    print("Resultado encontrado:", doc[start:end].text)
