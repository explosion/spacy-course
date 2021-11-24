import spacy
from spacy.tokens import Span

nlp = spacy.blank("de")

doc1 = nlp("Reddit und Patreon helfen Kreativen beim Aufbau von Communities")
doc1.ents = [
    Span(doc1, 0, 1, label="WEBSITE"),
    Span(doc1, 2, 3, label="WEBSITE"),
]

doc2 = nlp("PewDiePie knackt Rekord auf YouTube")
doc2.ents = [Span(doc2, 4, 5, label="WEBSITE")]

doc3 = nlp("Mitgründer von Reddit, Alexis Ohanian, schenkt Fans zwei Metallica-Tickets")
doc3.ents = [Span(doc3, 2, 3, label="WEBSITE")]

# Und so weiter...
