# Importa spaCy
import spacy

# Crea el objeto nlp para procesar alemán
nlp = spacy.blank("de")

# Procesa un texto (aquí dice "Saludos cordiales!" en alemán)
doc = nlp("Liebe Grüße!")

# Imprime en pantalla el texto del documento
print(doc.text)

