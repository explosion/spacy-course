import spacy

nlp = spacy.blank("pt")

# Importe a classe Doc
from spacy.tokens import Doc

# Texto desejado: "Oh, realmente?!"
words = ["Oh", ",", "realmente", "?", "!"]
spaces = [False, True, False, False, False]

# Crie um Doc a partir das palavras words e espaçamento spaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
