import spacy

#Crea un modelo "en" en blanco
nlp = spacy.blank("en")

# Crea un nuevo entity recognizer y añádelo al pipeline
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)

# Añade el label "GADGET" al entity recognizer
ner.add_label("GADGET")
