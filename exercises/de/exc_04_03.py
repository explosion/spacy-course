import json
from spacy.matcher import Matcher
from spacy.lang.de import German

with open("exercises/de/iphone.json") as f:
    TEXTS = json.loads(f.read())

nlp = German()
matcher = Matcher(nlp.vocab)

# Zwei Tokens, deren kleingeschriebene Formen "iphone" und "x" sind
pattern1 = [{____: ____}, {____: ____}]

# Token mit der kleingeschriebenen Form "iphone" und eine Ziffer
pattern2 = [{____: ____}, {____: ____}]

# Füge Patterns zum Matcher hinzu und überprüfe die Resultate
matcher.add("GADGET", None, pattern1, pattern2)
for doc in nlp.pipe(TEXTS):
    print([doc[start:end] for match_id, start, end in matcher(doc)])
