from spacy.lang.de import German
from spacy.tokens import Token

nlp = German()

# Registriere die Token-Erweiterung "is_country" mit default-Wert False
Token.set_extension("is_country", default=False)

# Verarbeite den Text und setze is_country auf True für den Token "Spanien"
doc = nlp("Ich wohne in Spanien.")
doc[3]._.is_country = True

# Drucke den Text und das Attribut is_country für alle Tokens
print([(token.text, token._.is_country) for token in doc])
