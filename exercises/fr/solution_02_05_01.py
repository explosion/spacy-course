import spacy

nlp = spacy.blank("fr")

# Importe la classe Doc
from spacy.tokens import Doc

# Texte désiré : "spaCy est cool."
words = ["spaCy", "est", "cool", "."]
spaces = [True, True, False, False]

# Crée un Doc à partir des mots et des espaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
