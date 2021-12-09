import json
import spacy
from spacy.tokens import Doc

with open("exercises/de/bookquotes.json", encoding="utf8") as f:
    DATA = json.loads(f.read())

nlp = spacy.blank("de")

# Registriere die Doc-Erweiterung "autor" (default: None)
____

# Registriere die Doc-Erweiterung "buch" (default: None)
____

for doc, ____ in ____(____, ____):
    # Überschreibe die Attribute doc._.buch und doc._.autor basierend auf dem Kontext
    doc._.buch = ____
    doc._.autor = ____

    # Drucke den Text und die Daten der benutzerdefinierten Attribute
    print(f"{doc.text}\n — '{doc._.buch}' von {doc._.autor}\n")
