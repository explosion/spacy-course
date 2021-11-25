# Importa spaCy
import spacy

# Crea el objeto nlp para procesar español
nlp = spacy.blank("es")

# Procesa un texto
doc = nlp("¿Cómo estás?")

# Imprime en pantalla el texto del documento
print(doc.text)
