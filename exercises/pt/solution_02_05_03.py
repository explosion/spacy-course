import spacy

nlp = spacy.blank("en")

# Importe a classe Doc
from spacy.tokens import Doc

# Texto desejado: "Oh, really?!"
words = ["Oh", ",", "really", "?", "!"]
spaces = [False, True, False, False, False]

# Crie um Doc a partir das palavras words e espaçamento spaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
