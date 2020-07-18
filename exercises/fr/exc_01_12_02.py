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

# Écris un motif qui recherche une forme de "download" suivie d'un nom propre
pattern = [{"LEMMA": ____}, {"POS": ____}]

# Ajoute le motif au matcher et applique le matcher au doc
matcher.add("DOWNLOAD_THINGS_PATTERN", None, pattern)
matches = matcher(doc)
print("Nombre de correspondances trouvées :", len(matches))

# Itère sur les correspondances et affiche la portion de texte
for match_id, start, end in matches:
    print("Correspondance trouvée : ", doc[start:end].text)
