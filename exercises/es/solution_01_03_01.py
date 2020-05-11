# Importa la clase de lenguaje "English" y crea el objeto nlp
from spacy.lang.en import English

nlp = English()

# Procesa el texto
doc = nlp("I like tree kangaroos and narwhals.")

# Selecciona el primer token
first_token = doc[0]

# Imprime en pantalla el texto del token
print(first_token.text)
