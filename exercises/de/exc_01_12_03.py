import spacy
from spacy.matcher import Matcher

nlp = spacy.load("de_core_news_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "Zu den Features der App gehören ein wunderschönes farbenfrohes Design, "
    "intelligente Suche, automatisierte Labels und Sprachsteuerung."
)

# Schreibe ein Pattern für ein Adjektiv, ein optionales Adjektiv und ein Nomen
pattern = [{"POS": ____}, {"POS": ____, "OP": ____}, {"POS": ____}]

# Füge das Pattern zum Matcher hinzu und wende den Matcher auf das Doc an
matcher.add("ADJ_NOUN_PATTERN", None, pattern)
matches = matcher(doc)
print("Anzahl an Resultaten:", len(matches))

# Iteriere über die Resultate und drucke den Text der Span
for match_id, start, end in matches:
    print("Resultat gefunden:", doc[start:end].text)
