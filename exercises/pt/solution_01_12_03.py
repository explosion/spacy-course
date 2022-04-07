import spacy
from spacy.matcher import Matcher

nlp = spacy.load("pt_core_news_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "Os recursos do aplicativo incluem um design bonito e moderno, busca inteligente, "
    " rótulos automáticos e resposta de voz opcional."
)

# Escreva uma expressão que corresponda a um substantivo seguido de um ou dois adjetivos
pattern = [{"POS": "NOUN"}, {"POS": "ADJ","OP":"?"},{"TEXT": "e","OP":"?"} ,{"POS": "ADJ"} ]

# Adicione uma expressão ao comparador matcher e aplique o matcher ao doc
matcher.add("ADJ_NOUN_PATTERN", [pattern])
matches = matcher(doc)
print("Total de correspondências encontradas:", len(matches))

# Faça a iteração sobre as correspondencias e imprima a partição do texto
for match_id, start, end in matches:
    print("Correspondências encontradas:", doc[start:end].text)
