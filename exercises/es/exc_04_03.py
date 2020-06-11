import json
from spacy.matcher import Matcher
from spacy.lang.es import Spanish

with open("exercises/es/adidas.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = Spanish()
matcher = Matcher(nlp.vocab)

# Dos tokens que en minúsculas encuentran "adidas" y "zx"
pattern1 = [{____: ____}, {____: ____}]

# Token que en minúsculas encuentra "adidas" y un dígito
pattern2 = [{____: ____}, {____: ____}]

# Añade los patrones al matcher y revisa el resultado
matcher.add("ROPA", None, pattern1, pattern2)
for doc in nlp.pipe(TEXTS):
    print([doc[start:end] for match_id, start, end in matcher(doc)])
