from spacy.lang.de import German
from spacy.tokens import Doc

nlp = German()

# Definiere die Getter-Funktion
def get_has_number(doc):
    # Gebe zurück, ob einer der Tokens im Doc True für token.like_num zurückgibt
    return any(token.like_num for token in doc)


# Registriere die Doc-Erweiterung "has_number" mit Getter-Funktion get_has_number
Doc.set_extension("has_number", getter=get_has_number)

# Verarbeite den Text und drucke den Wert des Attributs has_number
doc = nlp("Das Museum war ab 2012 fünf Jahre lang geschlossen.")
print("has_number:", doc._.has_number)
