import json
from spacy.matcher import Matcher
from spacy.lang.en import English

with open("exercises/en/iphone.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = English()
matcher = Matcher(nlp.vocab)
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]
matcher.add("GADGET", None, pattern1, pattern2)

TRAINING_DATA = []

# Criar um objeto Doc para cada frase em TEXTS
for doc in nlp.pipe(TEXTS):
    # Fazer a correspondência com o doc e criar uma lista com as partições que houve correspondência
    spans = [doc[start:end] for match_id, start, end in matcher(doc)]
    # Obter as tuplas (caracter inicial, caracter final, rótulo) das partições com correspondência
    entities = [(span.start_char, span.end_char, "GADGET") for span in spans]
    # Formatar as correspondência como uma tupla (doc.text, entities)
    training_example = (doc.text, {"entities": entities})
    # Adicionar o exemplo aos dados de treinamento
    TRAINING_DATA.append(training_example)

print(*TRAINING_DATA, sep="\n")
