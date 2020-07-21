import spacy
import random
import json

with open("exercises/fr/gadgets.json", encoding="utf8") as f:
    TRAINING_DATA = json.loads(f.read())

nlp = spacy.blank("fr")
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
ner.add_label("GADGET")

# Commence l'apprentissage
____.____

# Boucle pour 10 itérations
for itn in range(____):
    # Mélange les données d'apprentissage
    random.shuffle(TRAINING_DATA)
    losses = {}

    # Répartis les exemples en lots et itère dessus
    for batch in ____.____.____(TRAINING_DATA, size=2):
        texts = [____ for text, entities in batch]
        annotations = [____ for text, entities in batch]

        # Actualise le modèle
        ____.____(texts, annotations, losses=losses)
    print(losses)
