import spacy

# Erstelle ein leeres Model für "de"
nlp = spacy.blank("de")

# Erstelle einen neuen Entity Recognizer ("ner") und füge ihn zur Pipeline hinzu
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)

# Füge das Label "GADGET" zum Entity Recognizer hinzu
ner.add_label("GADGET")
