import spacy
from spacy.tokens import Span

nlp = spacy.load("pt_core_news_sm")


def get_wikipedia_url(span):
    # Gerar uma URL da Wikipedia se o texto tiver algum dos rótulos PERSON, ORG, GPE, LOCATION
    if ____ in ("PERSON", "ORG", "GPE", "LOCATION", "PER"):
        entity_text = span.text.replace(" ", "_")
        return "https://en.wikipedia.org/w/index.php?search=" + entity_text


# Definir a propriedade extendida wikipedia_url usando o atributo getter com get_wikipedia_url
____.____(____, ____=____)

doc = nlp(
    "Ao longo de cinquenta anos, desde o lançamento de suas primeira músicas até o último album, "
    " David Bowie sempre esteve na vanguarda da cultura contemporânea."
)
for ent in doc.ents:
    # Imprimir a entidade e URL da Wikipedia URL para a entidade
    print(____, ____)
