import spacy

nlp = spacy.blank("fr")

# Importe la classe Doc
from spacy.tokens import Doc

# Texte désiré : "Oh, vraiment ?!"
words = ["Oh", ",", "vraiment", "?", "!"]
spaces = [False, True, True, False, False]

# Crée un Doc à partir des mots et des espaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
