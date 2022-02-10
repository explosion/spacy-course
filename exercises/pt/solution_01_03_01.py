# Importar spacy e criar o objeto nlp do Português
import spacy
nlp = spacy.blank("pt")

# Processar o texto
doc = nlp("Eu gosto de gatos e cachorros.")

# Selecionar o primeiro token
first_token = doc[0]

# Imprimir o texto do primeito token
print(first_token.text)
