import spacy

nlp = spacy.load("es_core_news_sm")

# Importa la clase Doc
from spacy.tokens import Doc

# El texto deseado: "¡¿En serio?!"
words = ["¡", "¿", "En", "serio", "?", "!"]
spaces = [False, False, True, False, False, False]

# Crea un Doc a partir de las palabras y los espacios
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
