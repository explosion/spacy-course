# Importa spaCy y crea el objeto nlp para procesar español
import spacy

nlp = spacy.blank("es")

# Procesa el texto
doc = nlp("Me gustan las panteras negras y los leones.")

# Un slice del Doc para "panteras negras"
panteras_negras = doc[3:5]
print(panteras_negras.text)

# Un slice del Doc para "panteras negras y los leones" (sin el ".")
panteras_negras_y_leones = doc[3:8]
print(panteras_negras_y_leones.text)
