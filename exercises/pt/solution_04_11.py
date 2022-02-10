import spacy
from spacy.tokens import Span

nlp = spacy.blank("en")

doc1 = nlp("i went to amsterdem last year and the canals were beautiful")
doc1.ents = [Span(doc1, 3, 4, label="GPE")]

doc2 = nlp("You should visit Paris once, but the Eiffel Tower is kinda boring")
doc2.ents = [Span(doc2, 3, 4, label="GPE")]

doc3 = nlp("There's also a Paris in Arkansas, lol")
doc3.ents = [Span(doc3, 4, 5, label="GPE"), Span(doc3, 6, 7, label="GPE")]

doc4 = nlp("Berlin is perfect for summer holiday: great nightlife and cheap beer!")
doc4.ents = [Span(doc4, 0, 1, label="GPE")]
