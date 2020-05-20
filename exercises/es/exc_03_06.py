import spacy

# Define el componente personalizado
def length_component(doc):
    # Obtén la longitud del doc
    doc_length = ____
    print(f"This document is {doc_length} tokens long.")
    # Devuelve el doc
    ____


# Carga el modelo pequeño de inglés
nlp = spacy.load("en_core_web_sm")

# Añade el componente en el primer lugar del pipeline e imprime los nombres de los pipes en pantalla
____.____(____)
print(nlp.pipe_names)

# Procesa un texto
doc = ____
