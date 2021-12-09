import spacy
from spacy.tokens import Span

nlp = spacy.blank("es")

doc1 = nlp("Reddit hizo una alianza con Patreon para ayudar a los creadores",)
doc1.ents = [
    Span(doc1, 0, 1, label="WEBSITE"),
    Span(doc1, 5, 6, label="WEBSITE"),
]

doc2 = nlp("PewDiePie rompe el record de YouTube")
doc2.ents = [Span(doc2, 5, 6, label="WEBSITE")]

doc3 = nlp("El fundador de Reddit, Alexis Ohanian, regaló dos tiquetes de Metallica")
doc3.ents = [Span(doc3, 3, 4, label="WEBSITE")]

# y así sucesivamente...
