import spacy
from spacy.matcher import Matcher

nlp = spacy.load("pt_core_news_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "Eu baixei o Fortnite em meu computador e não consigo abrir o jogo de jeito algum. Me ajudem? "
    "Mas quando eu estava baixando o Minecraft, eu tinha a versão do Windows que é "
    "uma pasta .zip e eu usei o aplicativo padrão para descompactá-lo. Será que "
    "eu preciso baixar o Winzip também? "
)

# Escreva uma expressão que corresponda às variações de "baixar" seguido de um
# artigo e um substatantivo próprio
pattern = [{"LEMMA": ____},{"POS": ____},{"POS": ____}]

# Adicione a expressão ao comparador matcher e aplique o matcher ao doc
matcher.add("DOWNLOAD_THINGS_PATTERN", [pattern])
matches = matcher(doc)
print("Total de correspondências encontradas:", len(matches))

# Faça a iteração nas correspondências e imprima a partição do texto
for match_id, start, end in matches:
    print("Correspondência encontrada:", doc[start:end].text)
