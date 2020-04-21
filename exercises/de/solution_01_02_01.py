# Importiere die Klasse English
from spacy.lang.en import English

# Erstelle das nlp-Objekt
nlp = English()

# Verarbeite einen Text
doc = nlp("This is a sentence.")

# Drucke den Text des Dokuments
print(doc.text)
