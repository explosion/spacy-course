import json
from spacy.lang.de import German
from spacy.tokens import Doc

with open("exercises/de/bookquotes.json") as f:
    DATA = json.loads(f.read())

nlp = German()

# Registriere die Doc-Erweiterung "autor" (default: None)
Doc.set_extension("autor", default=None)

# Registriere die Doc-Erweiterung "buch" (default: None)
Doc.set_extension("buch", default=None)

for doc, context in nlp.pipe(DATA, as_tuples=True):
    # Überschreibe die Attribute doc._.buch und doc._.autor basierend auf dem Kontext
    doc._.buch = context["buch"]
    doc._.autor = context["autor"]

    # Drucke den Text und die Daten der benutzerdefinierten Attribute
    print(f"{doc.text}\n — '{doc._.buch}' von {doc._.autor}\n")
