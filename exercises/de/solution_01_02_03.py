# Importiere die Klasse Spanish
from spacy.lang.es import Spanish

# Erstelle das nlp-Objekt
nlp = Spanish()

# Verarbeite einen Text
doc = nlp("¿Cómo estás?")

# Drucke den Text des Dokuments
print(doc.text)
