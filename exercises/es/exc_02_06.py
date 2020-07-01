from spacy.lang.es import Spanish

nlp = Spanish()

# Importa las clases Doc y Span
from spacy.____ import ____, ____

words = ["Me", "gusta", "David", "Bowie"]
spaces = [True, True, True, False]

# Crea un doc a partir de las palabras y los espacios
doc = ____(____, ____, ____)
print(doc.text)

# Crea un span para "David Bowie" a partir del doc y asígnalo al label "PERSON"
span = ____(____, ____, ____, label=____)
print(span.text, span.label_)

# Añade el span a las entidades del doc
____.____ = [____]

# Imprime en pantalla el texto y los labels de las entidades
print([(ent.text, ent.label_) for ent in doc.ents])
