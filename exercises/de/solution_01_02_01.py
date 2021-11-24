# Importiere spaCy
import spacy

# Erstelle ein deutsches nlp-Objekt
nlp = spacy.blank("de")

# Verarbeite einen Text
doc = nlp("Liebe Grüße!")

# Drucke den Text des Dokuments
print(doc.text)
