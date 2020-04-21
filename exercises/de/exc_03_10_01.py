from spacy.lang.de import German
from spacy.tokens import Doc

nlp = German()

# Definiere die Getter-Funktion
def get_has_number(doc):
    # Gebe zurück, ob einer der Tokens im Doc True für token.like_num zurückgibt
    return any(____ for token in doc)


# Registriere die Doc-Erweiterung "has_number" mit Getter-Funktion get_has_number
____.____(____, ____=____)

# Verarbeite den Text und drucke den Wert des Attributs has_number
doc = nlp("Das Museum war ab 2012 fünf Jahre lang geschlossen.")
print("has_number:", ____)
