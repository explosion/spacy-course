import spacy

#Crea un modelo "es" en blanco
nlp = spacy.blank("es")

# Crea un nuevo entity recognizer y añádelo al pipeline
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)

# Añade el label "ROPA" al entity recognizer
ner.add_label("ROPA")
