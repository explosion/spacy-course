import spacy

nlp = spacy.blank("en")

# Importe a classe Doc
from spacy.tokens import Doc

# Texto desejado: "spaCy is cool!"
words = ["spaCy", "is", "cool", "!"]
spaces = [True, True, False, False]

# Crie um Doc a partir das palavras words e o espaçamento spaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
