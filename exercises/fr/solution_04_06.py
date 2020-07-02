import spacy

# Crée un modèle "en" vide
nlp = spacy.blank("en")

# Crée un nouvel entity recognizer et ajoute-le au pipeline
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)

# Ajoute le label "GADGET" à l'entity recognizer
ner.add_label("GADGET")
