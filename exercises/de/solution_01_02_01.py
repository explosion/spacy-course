# Importiere spaCy
from spacy.lang.en import English

# Erstelle ein englisches nlp-Objekt
nlp = spacy.blank("en")

# Verarbeite einen Text
doc = nlp("This is a sentence.")

# Drucke den Text des Dokuments
print(doc.text)
