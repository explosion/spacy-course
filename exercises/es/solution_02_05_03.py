import spacy

nlp = spacy.load("en_core_web_sm")

# Importa la clase Doc
from spacy.tokens import Doc

# El texto deseado: "Oh, really?!"
words = ["Oh", ",", "really", "?", "!"]
spaces = [False, True, False, False, False]

# Crea un Doc a partir de las palabras y los espacios
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
