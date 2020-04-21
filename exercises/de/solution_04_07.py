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
nlp.begin_training()

# Führe die Schleife 10 Mal aus
for itn in range(10):
    # Mische die Trainingsdaten
    random.shuffle(TRAINING_DATA)
    losses = {}

    # Teile die Beispiele in Batches auf und iteriere über die Batches
    for batch in spacy.util.minibatch(TRAINING_DATA, size=2):
        texts = [text for text, entities in batch]
        annotations = [entities for text, entities in batch]

        # Aktualisiere das Modell
        nlp.update(texts, annotations, losses=losses)
    print(losses)
