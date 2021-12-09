import spacy
import random
import json

with open("exercises/en/gadgets.json", encoding="utf8") as f:
    TRAINING_DATA = json.loads(f.read())

nlp = spacy.blank("en")
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
ner.add_label("GADGET")

# Iniciar o treinamento
nlp.begin_training()

# Ciclo de 10 iterações
for itn in range(10):
    # Embaralhar os dados de treinamento
    random.shuffle(TRAINING_DATA)
    losses = {}

    # Criar lotes com exemplos e iterar nos lotes
    for batch in spacy.util.minibatch(TRAINING_DATA, size=2):
        texts = [text for text, entities in batch]
        annotations = [entities for text, entities in batch]

        # Atualizar o modelo
        nlp.update(texts, annotations, losses=losses)
    print(losses)
