import spacy

nlp = spacy.load("es_core_news_sm")

# Importa la clase Doc
from spacy.tokens import Doc

# El texto deseado: "spaCy es divertido!"
words = ["spaCy", "es", "divertido", "!"]
spaces = [True, True, False, False]

# Crea un Doc a partir de las palabras y los espacios
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
