import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "i downloaded Fortnite on my laptop and can't open the game at all. Help? "
    "so when I was downloading Minecraft, I got the Windows version where it "
    "is the '.zip' folder and I used the default program to unpack it... do "
    "I also need to download Winzip?"
)

# Schreibe ein Pattern das eine Form von "download" plus Eigennamen (proper noun) findet
pattern = [{"LEMMA": ____}, {"POS": ____}]

# Füge das Pattern zum Matcher hinzu und wende den Matcher auf das Doc an
matcher.add("DOWNLOAD_THINGS_PATTERN", None, pattern)
matches = matcher(doc)
print("Anzahl an Resultaten:", len(matches))

# Iteriere über die Resultate und drucke den Text der Span
for match_id, start, end in matches:
    print("Resultat gefunden:", doc[start:end].text)
