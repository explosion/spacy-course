import json
from spacy.matcher import Matcher
from spacy.lang.en import English

with open("exercises/iphone.json") as f:
    TEXTS = json.loads(f.read())

nlp = English()
matcher = Matcher(nlp.vocab)

# Two tokens whose lowercase forms match 'iphone' and 'x'
pattern1 = [{____: ____}, {____: ____}]

# Token whose lowercase form matches 'iphone' and an optional digit
pattern2 = [{____: ____}, {____: ____, ___: ____}]

# Add patterns to the matcher
matcher.add("GADGET", None, pattern1, pattern2)
