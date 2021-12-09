# Importiere spaCy
import spacy

# Erstelle ein englisches nlp-Objekt
nlp = spacy.blank("en")

# Verarbeite einen Text
doc = nlp("This is a sentence.")

# Drucke den Text des Dokuments
print(doc.text)