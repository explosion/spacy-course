import json
from spacy.matcher import Matcher
from spacy.lang.en import English

with open("exercises/en/iphone.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = English()
matcher = Matcher(nlp.vocab)
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]
matcher.add("GADGET", [pattern1, pattern2])

TRAINING_DATA = []

# Create a Doc object for each text in TEXTS
for ____ in ____:
    # Match on the doc and create a list of matched spans
    spans = [____[____:____] for match_id, start, end in matcher(doc)]
    # Get (start character, end character, label) tuples of matches
    entities = [(span.start_char, span.end_char, "GADGET") for span in spans]
    # Format the matches as a (doc.text, entities) tuple
    training_example = (____, {"entities": ____})
    # Append the example to the training data
    ____.____(____)

print(*TRAINING_DATA, sep="\n")
