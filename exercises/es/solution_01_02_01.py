# Importa spaCy
import spacy

# Crea el objeto nlp para procesar inglés
nlp = spacy.blank("en")

# Procesa un texto (aquí dice "Esta es una oración" en inglés)
doc = nlp("This is a sentence.")

# Imprime en pantalla el texto del documento
print(doc.text)

