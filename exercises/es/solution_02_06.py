from spacy.lang.es import Spanish

nlp = Spanish()

# Importa las clases Doc y Span
from spacy.tokens import Doc, Span

words = ["Me", "gusta", "David", "Bowie"]
spaces = [True, True, True, False]

# Crea un Doc a partir de las palabras y los espacios
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

# Crea un span para "David Bowie" a partir del doc y asígnalo al label "PERSON"
span = Span(doc, 2, 4, label="PERSON")
print(span.text, span.label_)

# Añade el span a las entidades del doc
doc.ents = [span]

# Imprime en pantalla el texto y los labels de las entidades
print([(ent.text, ent.label_) for ent in doc.ents])
