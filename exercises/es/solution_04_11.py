import spacy
from spacy.tokens import Span

nlp = spacy.blank("es")

doc1 = nlp("El año pasado fuí a Venecie y los canales estaban hermosos")
doc1.ents = [Span(doc1, 5, 6, label="LOC")]

doc2 = nlp("Deberías visitar Madrid una vez en tu vida, "
           "pero el museo prado es aburrido")
doc2.ents = [Span(doc2, 2, 3, label="LOC"),
             Span(doc2, 11, 13, label="LOC")]

doc3 = nlp("Yo sé que también hay un Madrid en Colombia, jaja")
doc3.ents = [Span(doc3, 6, 7, label="LOC"), Span(doc3, 8, 9, label="LOC")]

doc4 = nlp("Una ciudad como Berlín es perfecta para las vacaciones de verano: "
           "muchos, parques, gran vida nocturna, cerveza barata!")
doc4.ents = [Span(doc4, 3, 4, label="LOC")]
