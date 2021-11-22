# Importiere spaCy und erstelle ein deutsches nlp-Objekt
import spacy

nlp = spacy.blank("de")

# Verarbeite den Text
doc = nlp("Ich mag niedliche Katzen und Faultiere.")

# Wähle den ersten Token aus
erster_token = doc[0]

# Drucke den Text des ersten Tokens
print(erster_token.text)
