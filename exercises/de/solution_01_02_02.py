# Importiere die Klasse German
from spacy.lang.de import German

# Erstelle das nlp-Objekt
nlp = German()

# Verarbeite einen Text
doc = nlp("Liebe Grüße!")

# Drucke den Text des Dokuments
print(doc.text)
