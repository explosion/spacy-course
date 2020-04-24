import spacy

nlp = spacy.load("en_core_web_sm")

# Importa la clase Doc
from spacy.tokens import Doc

# El texto deseado: "spaCy is cool!"
words = ["spaCy", "is", "cool", "!"]
spaces = [True, True, False, False]

# Crea un Doc a partir de las palabras y los espacios
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
