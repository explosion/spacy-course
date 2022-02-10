import spacy

nlp = spacy.blank("pt")

# Importe as classes Doc e Span 
from spacy.____ import ____, ____

words = ["Eu", "adoro", "David", "Bowie"]
spaces = [True, True, True, False]

# Crie um doc Doc a partir das palavras words e espaçamento spaces
doc = ____(____, ____, ____)
print(doc.text)

# Crie uma partição para "David Bowie" a partir do doc e atribua o marcador "PERSON"
span = ____(____, ____, ____, label=____)
print(span.text, span.label_)

# Adicione a partição às entidades do doc.
____.____ = [____]

# Imprima o texto e os marcadores das entidades
print([(ent.text, ent.label_) for ent in doc.ents])
