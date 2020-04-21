import spacy

# Importiere den Matcher
from spacy.____ import ____

nlp = spacy.load("de_core_news_sm")
doc = nlp("Das neue iPhone X erscheint demnächst in Deutschland")

# Initialisiere den Matcher mit dem gemeinsamen Vokabular
matcher = ____(____.____)

# Erstelle ein Pattern, das zwei Token findet: "iPhone" und "X"
pattern = [____]

# Füge das Pattern zum Matcher hinzu
____.____("IPHONE_X_PATTERN", None, ____)

# Wende den Matcher auf das Doc an
matches = ____
print("Resultat:", [doc[start:end].text for match_id, start, end in matches])
