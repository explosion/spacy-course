import json
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span

with open("exercises/es/adidas.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = spacy.blank("es")
matcher = Matcher(nlp.vocab)

# Dos tokens que en minúsculas encuentran "adidas" y "zx"
pattern1 = [{"LOWER": "adidas"}, {"LOWER": "zx"}]

# Token que en minúsculas encuentra "adidas" y un dígito
pattern2 = [{"LOWER": "adidas"}, {"IS_DIGIT": True}]

# Añade los patrones al matcher y revisa el resultado
matcher.add("ROPA", [pattern1, pattern2])
docs = []
for doc in nlp.pipe(TEXTS):
    matches = matcher(doc)
    spans = [Span(doc, start, end, label=match_id) for match_id, start, end in matches]
    print(spans)
    doc.ents = spans
    docs.append(doc)
