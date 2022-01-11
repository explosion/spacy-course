import spacy

nlp = spacy.blank("fr")

# Importe la classe Doc
from spacy.tokens import Doc

# Texte désiré : "Allez, on commence !"
words = ["Allez", ",", "on", "commence", "!"]
spaces = [False, True, True, True, False]

# Crée un Doc à partir des mots et des espaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
