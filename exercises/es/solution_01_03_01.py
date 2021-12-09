# Importa spaCy y crea el objeto nlp para procesar español
import spacy

nlp = spacy.blank("es")

# Procesa el texto
doc = nlp("Me gustan las panteras negras y los leones.")

# Selecciona el primer token
first_token = doc[0]

# Imprime en pantalla el texto del token
print(first_token.text)
