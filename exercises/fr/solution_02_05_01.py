from spacy.lang.en import English

nlp = English()

# Importe la classe Doc
from spacy.tokens import Doc

# Texte désiré : "spaCy is cool!"
words = ["spaCy", "is", "cool", "!"]
spaces = [True, True, False, False]

# Crée un Doc à partir des mots et des espaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
