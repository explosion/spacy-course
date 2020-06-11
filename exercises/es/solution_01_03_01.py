# Importa la clase de lenguaje "Spanish" y crea el objeto nlp
from spacy.lang.es import Spanish

nlp = Spanish()

# Procesa el texto
doc = nlp("Me gustan las panteras negras y los leones.")

# Selecciona el primer token
first_token = doc[0]

# Imprime en pantalla el texto del token
print(first_token.text)
