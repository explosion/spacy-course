import json
from spacy.lang.es import Spanish
from spacy.tokens import Doc

with open("exercises/es/bookquotes.json", encoding="utf8") as f:
    DATA = json.loads(f.read())

nlp = Spanish()

# Registra la extensión del Doc, "author" (por defecto None)
____

# Registra la extensión del Doc, "book" (por defecto None)
____

for doc, ____ in ____(____, ____):
    # Añade los atributos doc._.book y doc._.author desde el contexto
    doc._.book = ____
    doc._.author = ____

    # Imprime en pantalla el texto y los datos del atributo personalizado
    print(f"{doc.text}\n — '{doc._.book}' by {doc._.author}\n")
