import json
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span

with open("exercises/de/iphone.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = spacy.blank("de")
matcher = Matcher(nlp.vocab)

# Zwei Tokens, deren kleingeschriebene Formen "iphone" und "x" sind
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]

# Token mit der kleingeschriebenen Form "iphone" und eine Ziffer
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]

# Füge Patterns zum Matcher hinzu und erstelle Docs mit den Entitäten
matcher.add("GADGET", [pattern1, pattern2])
docs = []
for doc in nlp.pipe(TEXTS):
    matches = matcher(doc)
    spans = [Span(doc, start, end, label=match_id) for match_id, start, end in matches]
    print(spans)
    doc.ents = spans
    docs.append(doc)

