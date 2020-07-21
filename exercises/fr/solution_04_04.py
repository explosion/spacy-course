import json
from spacy.matcher import Matcher
from spacy.lang.fr import French

with open("exercises/fr/iphone.json") as f:
    TEXTS = json.loads(f.read())

nlp = French()
matcher = Matcher(nlp.vocab)
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]
matcher.add("GADGET", None, pattern1, pattern2)

TRAINING_DATA = []

# Crée un objet Doc pour chaque texte dans TEXTS
for doc in nlp.pipe(TEXTS):
    # Recherche les correspondances sur le doc
    # et crée une liste des spans correspondants
    spans = [doc[start:end] for match_id, start, end in matcher(doc)]
    # Obtiens les tuples (start character, end character, label)
    # des correspondances
    entities = [(span.start_char, span.end_char, "GADGET") for span in spans]
    # Formate les correspondances sous forme de tuple (doc.text, entities)
    training_example = (doc.text, {"entities": entities})
    # Ajoute l'exemple aux données d'apprentissage
    TRAINING_DATA.append(training_example)

print(*TRAINING_DATA, sep="\n")
