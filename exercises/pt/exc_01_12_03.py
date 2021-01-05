import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "Features of the app include a beautiful design, smart search, automatic "
    "labels and optional voice responses."
)

# Escreva uma expressão que corresponda a um adjetivo seguido de um ou dois substantivos
pattern = [{"POS": ____}, {"POS": ____}, {"POS": ____, "OP": ____}]

# Adicione uma expressão ao comparador matcher e aplique o matcher ao doc
matcher.add("ADJ_NOUN_PATTERN", None, pattern)
matches = matcher(doc)
print("Total matches found:", len(matches))

# Faça a iteração sobre as correspondencias e imprima a partição do texto
for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)
