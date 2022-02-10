import json
import spacy
from spacy.tokens import Doc

with open("exercises/en/bookquotes.json", encoding="utf8") as f:
    DATA = json.loads(f.read())

nlp = spacy.blank("en")

# Definir a propriedade customizada do Doc: "author" (default None)
____

# Definir a propriedade customizada do Doc: "book" (default None)
____

for doc, ____ in ____(____, ____):
    # Definir as propriedades doc._.book e doc._.author a partir do contexto
    doc._.book = ____
    doc._.author = ____

    # Imprimir o texto e as propriedades customizadas
    print(f"{doc.text}\n — '{doc._.book}' by {doc._.author}\n")
