import spacy

# Importiere den Matcher
from spacy.matcher import Matcher

nlp = spacy.load("de_core_news_sm")
doc = nlp("Das neue iPhone X erscheint demnächst in Deutschland")

# Initialisiere den Matcher mit dem gemeinsamen Vokabular
matcher = Matcher(nlp.vocab)

# Erstelle ein Pattern, das zwei Token findet: "iPhone" und "X"
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]

# Füge das Pattern zum Matcher hinzu
matcher.add("IPHONE_X_PATTERN", None, pattern)

# Wende den Matcher auf das Doc an
matches = matcher(doc)
print("Resultat:", [doc[start:end].text for match_id, start, end in matches])
