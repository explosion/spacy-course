from spacy.lang.de import German
from spacy.tokens import Token

nlp = German()

# Definiere die Getter-Funktion, die den umgekehrten Text eines Tokens zurückgibt
def get_reversed(token):
    return token.text[::-1]


# Registriere die Token-Erweiterung "reversed" mit Getter-Funktion get_reversed
Token.set_extension("reversed", getter=get_reversed)

# Verarbeite den Text und drucke den Text und das Attribut reversed für jeden Token
doc = nlp("Alle Verallgemeinerungen sind falsch, diese eingeschlossen.")
for token in doc:
    print("Umgekehrt:", token._.reversed)
