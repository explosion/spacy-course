import json
import spacy
from spacy.tokens import Doc

with open("exercises/en/bookquotes.json", encoding="utf8") as f:
    DATA = json.loads(f.read())

nlp = spacy.blank("en")

# Definir a propriedade customizada do Doc: "author" (default None)
Doc.set_extension("author", default=None)

# Definir a propriedade customizada do Doc: "book" (default None)
Doc.set_extension("book", default=None)

for doc, context in nlp.pipe(DATA, as_tuples=True):
    # Definir as propriedades doc._.book e doc._.author a partir do contexto
    doc._.book = context["book"]
    doc._.author = context["author"]

    # Imprimir o texto e as propriedades customizadas
    print(f"{doc.text}\n — '{doc._.book}' by {doc._.author}\n")
