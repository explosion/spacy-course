import spacy

nlp = spacy.blank("pt")

# Importe a classe Doc
from spacy.tokens import Doc

# Texto desejado: "spaCy é bem legal!"
words = ["spaCy", "é", "bem","legal","!"]
spaces = [True, True, True, False, False]

# Crie um Doc a partir das palavras words e o espaçamento spaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
