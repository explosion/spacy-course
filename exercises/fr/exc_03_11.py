import spacy
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")


def get_wikipedia_url(span):
    # Retourne une URL Wikipédia si le span possède un des libellés
    if ____ in ("PERSON", "ORG", "GPE", "LOCATION"):
        entity_text = span.text.replace(" ", "_")
        return "https://en.wikipedia.org/w/index.php?search=" + entity_text


# Définis l'extension de Span wikipedia_url avec le getter get_wikipedia_url
____.____(____, ____=____)

doc = nlp(
    "In over fifty years from his very first recordings right through to his "
    "last album, David Bowie was at the vanguard of contemporary culture."
)
for ent in doc.ents:
    # Affiche le text et l'URL Wikipédia de l'entité
    print(____, ____)
