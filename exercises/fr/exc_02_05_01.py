from spacy.lang.en import English

nlp = English()

# Importe la classe Doc
from ____ import ____

# Texte désiré : "spaCy is cool!"
words = ["spaCy", "is", "cool", "!"]
spaces = [True, True, False, False]

# Crée un Doc à partir des mots et des espaces
doc = ____(____, words=words, spaces=spaces)
print(doc.text)
