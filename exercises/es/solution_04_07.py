import spacy
import random
import json

with open("exercises/en/gadgets.json") as f:
    TRAINING_DATA = json.loads(f.read())

nlp = spacy.blank("en")
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
ner.add_label("GADGET")

# Comienza el entrenamiento
nlp.begin_training()

# Haz un loop por 10 iteraciones
for itn in range(10):
    # Mezcla los datos de entrenamiento
    random.shuffle(TRAINING_DATA)
    losses = {}

    # Crea lotes con los ejemplos e itera sobre ellos
    for batch in spacy.util.minibatch(TRAINING_DATA, size=2):
        texts = [text for text, entities in batch]
        annotations = [entities for text, entities in batch]

        # Actualiza el modelo
        nlp.update(texts, annotations, losses=losses)
    print(losses)
