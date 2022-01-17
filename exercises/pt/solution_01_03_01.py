# Importar spacy e criar o objeto nlp do Inglês
import spacy
nlp = spacy.blank("en")

# Processar o texto
doc = nlp("I like tree kangaroos and narwhals.")

# Selecionar o primeiro token
first_token = doc[0]

# Imprimir o texto do primeito token
print(first_token.text)
