import spacy

# Define el componente personalizado
def length_component(doc):
    # Obtén la longitud del doc
    doc_length = len(doc)
    print(f"This document is {doc_length} tokens long.")
    # Devuelve el doc
    return doc


# Carga el modelo pequeño de inglés
nlp = spacy.load("en_core_web_sm")

# Añade el componente en el primer lugar del pipeline e imprime los nombres de los pipes en pantalla
nlp.add_pipe(length_component, first=True)
print(nlp.pipe_names)

# Procesa un texto
doc = nlp("This is a sentence.")
