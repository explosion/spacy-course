import spacy
import random
import json

with open("exercises/en/gadgets.json") as f:
    TRAINING_DATA = json.loads(f.read())

nlp = spacy.blank("en")
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
ner.add_label("GADGET")

# Commence l'apprentissage
nlp.begin_training()

# Boucle pour 10 itérations
for itn in range(10):
    # Mélange les données d'apprentissage
    random.shuffle(TRAINING_DATA)
    losses = {}

    # Répartis les exemples en lots et itère dessus
    for batch in spacy.util.minibatch(TRAINING_DATA, size=2):
        texts = [text for text, entities in batch]
        annotations = [entities for text, entities in batch]

        # Actualise le modèle
        nlp.update(texts, annotations, losses=losses)
    print(losses)
