from spacy.lang.de import German

nlp = German()

# Importiere die Klassen Doc und Span
from spacy.tokens import Doc, Span

words = ["Ich", "mag", "David", "Bowie"]
spaces = [True, True, True, False]

# Erstelle ein Doc mit den Wörtern und Leerzeichen
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

# Erstelle eine Span für "David Bowie" und weise ihr das Label "PER" zu
span = Span(doc, 2, 4, label="PER")
print(span.text, span.label_)

# Füge die Span zu den Entitäten des Docs hinzu
doc.ents = [span]

# Drucke den Text und Label der Entitäten
print([(ent.text, ent.label_) for ent in doc.ents])
