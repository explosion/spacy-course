import json
from spacy.matcher import Matcher
from spacy.lang.en import English

with open("exercises/en/iphone.json") as f:
    TEXTS = json.loads(f.read())

nlp = English()
matcher = Matcher(nlp.vocab)

# Dos tokens que en minúsculas encuentran "iphone" y "x"
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]

# Token que en minúsculas encuentra "iphone" y un dígito
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]

# Añade los patrones al matcher y revisa el resultado
matcher.add("GADGET", None, pattern1, pattern2)
for doc in nlp.pipe(TEXTS):
    print([doc[start:end] for match_id, start, end in matcher(doc)])
