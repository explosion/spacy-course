# Importiere die Klasse German und erstelle das nlp-Objekt
from spacy.lang.de import German

nlp = German()

# Verarbeite den Text
doc = nlp("Ich mag niedliche Katzen und Faultiere.")

# Wähle den ersten Token aus
erster_token = doc[0]

# Drucke den Text des ersten Tokens
print(erster_token.text)
