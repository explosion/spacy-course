# Importa la clase de lenguaje "Spanish"
from spacy.lang.es import Spanish

# Crea el objeto nlp
nlp = Spanish()

# Procesa un texto
doc = nlp("¿Cómo estás?")

# Imprime en pantalla el texto del documento
print(doc.text)
