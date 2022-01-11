import spacy

nlp = spacy.blank("fr")

# Importe la classe Doc
from ____ import ____

# Texte désiré : "spaCy est cool."
words = ["spaCy", "est", "cool", "."]
spaces = [True, True, False, False]

# Crée un Doc à partir des mots et des espaces
doc = ____(____, words=words, spaces=spaces)
print(doc.text)
