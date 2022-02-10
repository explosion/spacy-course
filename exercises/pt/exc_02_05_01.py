import spacy

nlp = spacy.blank("pt")

# Importe a classe Doc
from ____ import ____

# Texto desejado: "spaCy é bem legal!"
words = ["spaCy", "é", "bem","legal","!"]
spaces = [True, True, True, False, False]

# Crie um Doc a partir das palavras words e o espaçamento spaces
doc = ____(____, words=words, spaces=spaces)
print(doc.text)
