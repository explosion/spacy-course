import json
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span

with open("exercises/en/iphone.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = spacy.blank("en")
matcher = Matcher(nlp.vocab)

# Dois tokens cujo formato em minúsculas corresponda a "iphone" e "x"
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]

# Token cujo formato em minísculas corresponda a "iphone" e um dígito
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]

# Adicione as expressões ao Matcher e crie docs com as entidades com correspondência
matcher.add("GADGET", [pattern1, pattern2])
docs = []
for doc in nlp.pipe(TEXTS):
    matches = matcher(doc)
    spans = [Span(doc, start, end, label=match_id) for match_id, start, end in matches]
    print(spans)
    doc.ents = spans
    docs.append(doc)
