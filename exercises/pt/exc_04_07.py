import spacy
import random
import json

with open("exercises/en/gadgets.json") as f:
    TRAINING_DATA = json.loads(f.read())

nlp = spacy.blank("en")
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
ner.add_label("GADGET")

# Iniciar o treinamento
____.____

# Ciclo de 10 iterações
for itn in range(____):
    # Embaralhar os dados de treinamento
    random.shuffle(TRAINING_DATA)
    losses = {}

    # Criar lotes com exemplos e iterar nos lotes
    for batch in ____.____.____(TRAINING_DATA, size=2):
        texts = [____ for text, entities in batch]
        annotations = [____ for text, entities in batch]

        # Atualizar o modelo
        ____.____(texts, annotations, losses=losses)
    print(losses)
