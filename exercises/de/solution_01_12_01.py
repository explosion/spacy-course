import spacy
from spacy.matcher import Matcher

nlp = spacy.load("de_core_news_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "Dieses Update von iOS ist kein radikales, systemweites Redesign und kein "
    "Vergleich zum ästhetischen Erlebnis beim iOS 7 Upgrade. Der Großteil der "
    "Ausstattung von iOS 11 im Vergleich zu der von iOS 10 ist gleich geblieben."
)

# Schreibe ein Pattern für komplette iOS-Versionen ("iOS 7", "iOS 11", "iOS 10")
pattern = [{"TEXT": "iOS"}, {"IS_DIGIT": True}]

# Füge das Pattern zum Matcher hinzu und wende den Matcher auf das Doc an
matcher.add("IOS_VERSION_PATTERN", [pattern])
matches = matcher(doc)
print("Anzahl an Resultaten:", len(matches))

# Iteriere über die Resultate und drucke den Text der Span
for match_id, start, end in matches:
    print("Resultat gefunden:", doc[start:end].text)
