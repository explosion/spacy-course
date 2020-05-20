# Importa la clase de lenguaje "English"
from spacy.lang.en import English

# Crea el objeto nlp
nlp = English()

# Procesa un texto (aquí dice "Esto es una frase." en inglés)
doc = nlp("This is a sentence.")

# Imprime en pantalla el texto del documento
print(doc.text)
