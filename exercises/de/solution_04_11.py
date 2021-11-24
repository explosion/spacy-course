import spacy
from spacy.tokens import Span

nlp = spacy.blank("de")

doc1 = nlp("ich war letztes jahr in amsterdem und die kanäle warn superschön")
doc1.ents = [Span(doc1, 5, 6, label="LOC")]

doc2 = nlp("Du solltest einmal im Leben Paris besuchen, aber der Eiffelturm ist relativ langweilig")
doc2.ents = [Span(doc2, 5, 6, label="LOC")]

doc3 = nlp("Es gibt auch ein Paris in Arkansas lol")
doc3.ents = [Span(doc3, 4, 5, label="LOC"), Span(doc3, 6, 7, label="LOC")]

doc4 = nlp("Berlin ist perfekt für einen Sommerurlaub: viele Parks, tolles Nachleben, günstiges Bier!")
doc4.ents = [Span(doc4, 0, 1, label="LOC")]

