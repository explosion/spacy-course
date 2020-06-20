from spacy.lang.en import English

nlp = English()

# Importe les classes Doc et Span
from spacy.____ import ____, ____

words = ["I", "like", "David", "Bowie"]
spaces = [True, True, True, False]

# Crée un doc à partir des mots et des espaces
doc = ____(____, ____, ____)
print(doc.text)

# Crée un span pour "David Bowie" à partir du doc
# et assigne-lui le libellé "PERSON"
span = ____(____, ____, ____, label=____)
print(span.text, span.label_)

# Ajoute le span aux entités du doc
____.____ = [____]

# Affiche les textes et les libellés des entités
print([(ent.text, ent.label_) for ent in doc.ents])
