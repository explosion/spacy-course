import json
from spacy.matcher import Matcher
from spacy.lang.en import English

with open("exercises/en/iphone.json") as f:
    TEXTS = json.loads(f.read())

nlp = English()
matcher = Matcher(nlp.vocab)

# Dois tokens cujo formato em minúsculas corresponda a "iphone" e "x"
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]

# Token cujo formato em minísculas corresponda a "iphone" e um dígito
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]

# Adicione as expressões ao Matcher e verifique o resultado
matcher.add("GADGET", None, pattern1, pattern2)
for doc in nlp.pipe(TEXTS):
    print([doc[start:end] for match_id, start, end in matcher(doc)])
