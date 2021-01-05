# Importar a classe da língua inglesa (English) e criar um objeto nlp
from spacy.lang.en import English
nlp = English()

# Processar o texto
doc = nlp("I like tree kangaroos and narwhals.")

# Selecionar o primeiro token
first_token = doc[0]

# Imprimir o texto do primeito token
print(first_token.text)
