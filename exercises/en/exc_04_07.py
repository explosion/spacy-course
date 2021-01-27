import spacy
import random
import json

with open("exercises/en/gadgets.json", encoding="utf8") as f:
    TRAINING_DATA = json.loads(f.read())

nlp = spacy.blank("en")
ner = nlp.add_pipe("ner")
ner.add_label("GADGET")

# Start the training
____.____

# Loop for 10 iterations
for itn in range(____):
    # Shuffle the training data
    random.shuffle(TRAINING_DATA)
    losses = {}

    # Batch the examples and iterate over them
    for batch in ____.____.____(TRAINING_DATA, size=2):
        texts = [____ for text, entities in batch]
        annotations = [____ for text, entities in batch]

        # Update the model
        ____.____(texts, annotations, losses=losses)
    print(losses)
