import spacy
from spacy.tokens import Span

nlp = spacy.load("fr_core_news_sm")


def get_wikipedia_url(span):
    # Retourne une URL Wikipédia si le span possède un des libellés
    if span.label_ in ("PER", "ORG", "GPE", "LOCATION"):
        entity_text = span.text.replace(" ", "_")
        return "https://fr.wikipedia.org/w/index.php?search=" + entity_text


# Définis l'extension de Span wikipedia_url avec le getter get_wikipedia_url
Span.set_extension("wikipedia_url", getter=get_wikipedia_url)

doc = nlp(
    "Pendant plus de cinquante ans depuis ses tout premiers enregistrements "
    "jusqu'à son dernier album, David Bowie a toujours été à l'avant-garde "
    "de la culture contemporaine."
)
for ent in doc.ents:
    # Affiche le text et l'URL Wikipédia de l'entité
    print(ent.text, ent._.wikipedia_url)
