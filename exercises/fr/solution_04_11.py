import spacy
from spacy.tokens import Span

nlp = spacy.blank("fr")

doc1 = nlp("je suis allé à amsterdem l'an dernier et les canaux étaient magnifiques")
doc1.ents = [Span(doc1, 4, 5, label="GPE")]

doc2 = nlp("Tu devrais visiter Paris au moins une fois dans ta vie, "
    "mais la Tour Eiffel ce n'est pas terrible")
doc2.ents = [Span(doc2, 3, 4, label="GPE")]

doc3 = nlp("Il y a aussi un Paris dans l'Arkansas, lol")
doc3.ents = [Span(doc3, 5, 6, label="GPE"), Span(doc3, 8, 9, label="GPE")]

doc4 = nlp("Berlin est la destination parfaite pour les vacances d'été : "
    "beaucoup de parcs, une vie nocturne trépidante et de la bière pas chère !")
doc4.ents = [Span(doc4, 0, 1, label="GPE")]