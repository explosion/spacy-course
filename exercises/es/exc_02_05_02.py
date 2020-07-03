import spacy

nlp = spacy.load("es_core_news_sm")

# Importa la clase Doc
from ____ import ____

# El texto deseado: "¡Vamos, empieza!"
words = ["¡", "Vamos", ",", "empieza", "!"]
spaces = [____, ____, ____, ____, ____]

# Crea un Doc a partir de las palabras y los espacios
doc = ____(____, ____=____, ____=____)
print(doc.text)
