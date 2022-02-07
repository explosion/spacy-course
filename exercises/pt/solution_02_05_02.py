import spacy

nlp = spacy.blank("pt")

# Importe a classe Doc
from spacy.tokens import Doc

# Texto desejado: "Vamos lá, vamos começar!"
words = ["Vamos","lá", ",", "vamos", "começar", "!"]
spaces = [True, False, True, True, False, False]

# Crie um Doc a partir das palavras words e espaçamento spaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
