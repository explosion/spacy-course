import spacy

# Create a blank "en" model
nlp = spacy.blank("en")

# Create a new entity recognizer and add it to the pipeline
ner = nlp.add_pipe("ner")

# Add the label "GADGET" to the entity recognizer
ner.add_label("GADGET")
