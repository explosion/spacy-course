import json
import spacy
from spacy.tokens import Doc

with open("exercises/fr/bookquotes.json", encoding="utf8") as f:
    DATA = json.loads(f.read())

nlp = spacy.blank("fr")

# Déclare l'extension de Doc "author" (défaut None)
____

# Déclare l'extension de Doc "book" (default None)
____

for doc, ____ in ____(____, ____):
    # Définis les attributs doc._.book et doc._.author à partir du contexte
    doc._.book = ____
    doc._.author = ____

    # Affiche le texte et les données des attributs personnalisés
    print(f"{doc.text}\n — '{doc._.book}' par {doc._.author}\n")
