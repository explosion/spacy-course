import json
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span

with open("exercises/fr/iphone.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = spacy.blank("fr")
matcher = Matcher(nlp.vocab)

# Deux tokens dont les formes majuscules correspondent à "iphone" et "x"
pattern1 = [{____: ____}, {____: ____}]

# Tokens dont les formes majuscules correspondent à "iphone" et un nombre
pattern2 = [{____: ____}, {____: ____}]

# Ajoute les motifs au matcher et crée des docs avec les entités en correspondance
matcher.add("GADGET", [pattern1, pattern2])
docs = []
for doc in nlp.pipe(TEXTS):
    matches = matcher(doc)
    spans = [Span(doc, start, end, label=match_id) for match_id, start, end in matches]
    print(spans)
    doc.ents = spans
    docs.append(doc)
