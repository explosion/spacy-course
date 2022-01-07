import spacy
from spacy.tokens import Span

nlp = spacy.blank("fr")

doc1 = nlp("Reddit noue un partenariat avec Patreon pour aider les créateurs à former des communautés")
doc1.ents = [
    Span(doc1, 0, 1, label="SITE_WEB"),
    Span(doc1, 5, 6, label="SITE_WEB"),
]

doc2 = nlp("PewDiePie explose le record de YouTube")
doc2.ents = [Span(doc2, 5, 6, label="SITE_WEB")]

doc3 = nlp("Le fondateur de Reddit Alexis Ohanian a donné deux billets pour Metallica à des fans")
doc3.ents = [Span(doc3, 3, 4, label="SITE_WEB")]

# Et ainsi de suite...