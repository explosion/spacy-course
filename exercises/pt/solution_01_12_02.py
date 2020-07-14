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

# Escreva um padrão que corresponda às variações de "download" seguido de um
# substatantivo próprio
pattern = [{"LEMMA": "download"}, {"POS": "PROPN"}]

# Adicione o padrão ao combinador matcher e aplique o matcher ao doc
matcher.add("DOWNLOAD_THINGS_PATTERN", None, pattern)
matches = matcher(doc)
print("Total matches found:", len(matches))

# Faça a iteração nas correspondências e imprima a partição do texto
for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)
