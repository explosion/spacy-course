from spacy.lang.de import German
from spacy.tokens import Token

nlp = German()

# Registriere die Token-Erweiterung "is_country" mit default-Wert False
____.____(____, ____=____)

# Verarbeite den Text und setze is_country auf True für den Token "Spanien"
doc = nlp("Ich wohne in Spanien.")
____ = True

# Drucke den Text und das Attribut is_country für alle Tokens
print([(____, ____) for token in doc])
