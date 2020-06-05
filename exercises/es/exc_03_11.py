import spacy
from spacy.tokens import Span

nlp = spacy.load("es_core_news_sm")


def get_wikipedia_url(span):
    # Obtén la URL de Wikipedia si el span tiene uno de los siguientes labels
    if ____ in ("PER", "ORG", "LOC"):
        entity_text = span.text.replace(" ", "_")
        return "https://es.wikipedia.org/w/index.php?search=" + entity_text


# Añade la extensión del Span, wikipedia_url, usando el getter get_wikipedia_url
____.____(____, ____=____)

doc = nlp(
    "Antes de finalizar 1976, el interés de David Bowie en la "
    "floreciente escena musical alemana, le llevó a mudarse a "
    "Alemania para revitalizar su carrera."
)
for ent in doc.ents:
    # Imprime en pantalla el texto y la URL de Wikipedia de la entidad
    print(____, ____)
