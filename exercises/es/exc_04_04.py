import json
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span, DocBin

with open("exercises/es/adidas.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = spacy.blank("es")
matcher = Matcher(nlp.vocab)
# Agrega patrones al matcher
pattern1 = [{"LOWER": "adidas"}, {"LOWER": "zx"}]
pattern2 = [{"LOWER": "adidas"}, {"IS_DIGIT": True}]
matcher.add("ROPA", [pattern1, pattern2])
docs = []
for doc in nlp.pipe(TEXTS):
    matches = matcher(doc)
    spans = [Span(doc, start, end, label=match_id) for match_id, start, end in matches]
    doc.ents = spans
    docs.append(doc)

doc_bin = ____(____=____)
doc_bin.____(____)
