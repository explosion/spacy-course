import spacy

nlp = spacy.load("en_core_web_sm")

# Importa la clase Doc
from ____ import ____

# El texto deseado: "Oh, really?!"
words = [____, ____, ____, ____, ____]
spaces = [____, ____, ____, ____, ____]

# Crea un Doc a partir de las palabras y los espacios
doc = ____(____, ____=____, ____=____)
print(doc.text)
