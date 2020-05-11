# Importa la clase de lenguaje "German"
from spacy.lang.de import German

# Crea el objeto nlp
nlp = German()

# Procesa un texto (aquí dice "Saludos cordiales!" en alemán)
doc = nlp("Liebe Grüße!")

# Imprime en pantalla el texto del documento
print(doc.text)
