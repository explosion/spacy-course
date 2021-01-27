import spacy
from spacy.training import Example
import random
import json

with open("exercises/en/gadgets.json", encoding="utf8") as f:
    TRAINING_DATA = json.loads(f.read())

nlp = spacy.blank("en")
ner = nlp.add_pipe("ner")
ner.add_label("GADGET")

# Start the training
nlp.initialize()

# Loop for 10 iterations
for itn in range(10):
    # Shuffle the training data
    random.shuffle(TRAINING_DATA)
    losses = {}

    # Batch the examples and iterate over them
    for batch in spacy.util.minibatch(TRAINING_DATA, size=2):
        examples = []
        for text, annotations in batch:
            examples.append(Example.from_dict(nlp.make_doc(text), annotations))

        # Update the model
        nlp.update(examples, losses=losses)
    print(losses)
