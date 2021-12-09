from spacy.lang.en import English

nlp = English()

# Importe a classe Doc
from ____ import ____

# Texto desejado: "spaCy is cool!"
words = ["spaCy", "is", "cool", "!"]
spaces = [True, True, False, False]

# Crie um Doc a partir das palavras words e o espaçamento spaces
doc = ____(____, words=words, spaces=spaces)
print(doc.text)
