import spacy

# Carga el modelo en_core_web_sm
nlp = spacy.load("en_core_web_sm")

# Imprime en pantalla los nombres de los componentes del pipeline
print(nlp.pipe_names)

# Imprime en pantalla el pipeline entero de tuples (nombre, componente)
print(nlp.pipeline)
