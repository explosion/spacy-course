from spacy.lang.de import German

nlp = German()

# Importiere die Klasse Doc
from ____ import ____

# Erwarteter Text: "spaCy ist cool!"
words = ["spaCy", "ist", "cool", "!"]
spaces = [True, True, False, False]

# Erstelle ein Doc mit den Wörtern und Leerzeichen
doc = ____(____, words=words, spaces=spaces)
print(doc.text)
