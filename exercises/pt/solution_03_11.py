import spacy
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")


def get_wikipedia_url(span):
    # Gerar uma URL da Wikipedia se o texto tiver algum dos rótulos PERSON, ORG, GPE, LOCATION
    if span.label_ in ("PERSON", "ORG", "GPE", "LOCATION"):
        entity_text = span.text.replace(" ", "_")
        return "https://en.wikipedia.org/w/index.php?search=" + entity_text


# Definir a propriedade extendida wikipedia_url usando o atributo getter com get_wikipedia_url
Span.set_extension("wikipedia_url", getter=get_wikipedia_url)

doc = nlp(
    "In over fifty years from his very first recordings right through to his "
    "last album, David Bowie was at the vanguard of contemporary culture."
)
for ent in doc.ents:
    # Imprimir a entidade e URL da Wikipedia URL para a entidade
    print(ent.text, ent._.wikipedia_url)
