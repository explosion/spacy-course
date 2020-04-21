import spacy
import random
import json

with open("exercises/de/gadgets.json") as f:
    TRAINING_DATA = json.loads(f.read())

nlp = spacy.blank("de")
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
ner.add_label("GADGET")

# Beginne das Training
____.____

# Führe die Schleife 10 Mal aus
for itn in range(____):
    # Mische die Trainingsdaten
    random.shuffle(TRAINING_DATA)
    losses = {}

    # Teile die Beispiele in Batches auf und iteriere über die Batches
    for batch in ____.____.____(TRAINING_DATA, size=2):
        texts = [____ for text, entities in batch]
        annotations = [____ for text, entities in batch]

        # Aktualisiere das Modell
        ____.____(texts, annotations, losses=losses)
    print(losses)
