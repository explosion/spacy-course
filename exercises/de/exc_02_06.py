from spacy.lang.de import German

nlp = German()

# Importiere die Klassen Doc und Span
from spacy.____ import ____, ____

words = ["Ich", "mag", "David", "Bowie"]
spaces = [True, True, True, False]

# Erstelle ein Doc mit den Wörtern und Leerzeichen
doc = ____(____, ____, ____)
print(doc.text)

# Erstelle eine Span für "David Bowie" und weise ihr das Label "PER" zu
span = ____(____, ____, ____, label=____)
print(span.text, span.label_)

# Füge die Span zu den Entitäten des Docs hinzu
____.____ = [____]

# Drucke den Text und Label der Entitäten
print([(ent.text, ent.label_) for ent in doc.ents])
