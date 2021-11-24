# Importiere spaCy
import spacy

# Erstelle ein spanisches nlp-Objekt
nlp = spacy.blank("es")

# Verarbeite einen Text
doc = nlp("¿Cómo estás?")

# Drucke den Text des Dokuments
print(doc.text)
