# Importiere die Klasse German und erstelle das nlp-Objekt
from spacy.lang.de import German

nlp = German()

# Verarbeite den Text
doc = nlp("Ich mag niedliche Katzen und Faultiere.")

# Ein Abschnitt des Docs für "niedliche Katzen"
niedliche_katzen = doc[2:4]
print(niedliche_katzen.text)

# Ein Abschnitt des Docs für "niedliche Katzen und Faultiere" (ohne ".")
niedliche_katzen_und_faultiere = doc[2:6]
print(niedliche_katzen_und_faultiere.text)
