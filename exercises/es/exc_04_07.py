import spacy
import random
import json

with open("exercises/es/ropa.json", encoding="utf8") as f:
    TRAINING_DATA = json.loads(f.read())

nlp = spacy.blank("es")
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
ner.add_label("ROPA")

# Comienza el entrenamiento
____.____

# Haz un loop por 10 iteraciones
for itn in range(____):
    # Mezcla los datos de entrenamiento
    random.shuffle(TRAINING_DATA)
    losses = {}

    # Crea lotes con los ejemplos e itera sobre ellos
    for batch in ____.____.____(TRAINING_DATA, size=2):
        texts = [____ for text, entities in batch]
        annotations = [____ for text, entities in batch]

        # Actualiza el modelo
        ____.____(texts, annotations, losses=losses)
    print(losses)
