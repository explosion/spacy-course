import json
from spacy.matcher import Matcher
from spacy.lang.es import Spanish

with open("exercises/es/adidas.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = Spanish()
matcher = Matcher(nlp.vocab)
pattern1 = [{"LOWER": "adidas"}, {"LOWER": "zx"}]
pattern2 = [{"LOWER": "adidas"}, {"IS_DIGIT": True}]
matcher.add("ROPA", None, pattern1, pattern2)

TRAINING_DATA = []

# Crea un objeto Doc para cada texto en TEXTS
for ____ in ____:
    # Encuentra en el doc y crea una lista de los spans resultantes
    spans = [____[____:____] for match_id, start, end in matcher(doc)]
    # Obtén los tuples (carácter de inicio, carácter del final, label) resultantes
    entities = [(span.start_char, span.end_char, "ROPA") for span in spans]
    # Da formato a los resultados como tuples con (doc.text, entidades)
    training_example = (____, {"entities": ____})
    # Añade el ejemplo a los datos de entrenamiento
    ____.____(____)

print(*TRAINING_DATA, sep="\n")
