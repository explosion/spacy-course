import spacy
from spacy.matcher import Matcher

nlp = spacy.load("pt_core_news_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "Após fazer a atualização do iOS você não irá perceber uma mudança radical "
    "na sua interface: nada parecido com a reviravolta estética que foi feita com o iOS 7. A "
    "maioria da roupagem do iOS 11 permanece a mesma que o iOS 10. Mas você irá descobrir "
    "alguns ajustes se você procurar nos detalhes."
)

# Escreva uma expressão que corresponda às versões completas do IOS ("iOS 7", "iOS 11", "iOS 10")
pattern = [{"TEXT": "iOS"}, {"IS_DIGIT": True}]

# Adicione a expressão ao comparador matcher e aplique o matcher ao doc
matcher.add("IOS_VERSION_PATTERN", [pattern])
matches = matcher(doc)
print("Total de correspondências encontradas:", len(matches))

# Faça a iteração sobre as correspondencias e imprima a partição do texto
for match_id, start, end in matches:
    print("Correspondência encontrada:", doc[start:end].text)
