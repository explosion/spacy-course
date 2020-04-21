from spacy.lang.de import German

nlp = German()

# Importiere die Klasse Doc
from spacy.tokens import Doc

# Erwarteter Text: "Na, alles klar?"
words = ["Na", ",", "alles", "klar", "?"]
spaces = [False, True, True, False, False]

# Erstelle ein Doc mit den Wörtern und Leerzeichen
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
