import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
import json

with open("exercises/en/countries.json") as f:
    COUNTRIES = json.loads(f.read())
with open("exercises/en/country_text.txt") as f:
    TEXT = f.read()

nlp = spacy.load("en_core_web_sm")
matcher = PhraseMatcher(nlp.vocab)
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", None, *patterns)

# Crée un doc et réinitialise les entités existantes
doc = nlp(TEXT)
doc.ents = []

# Itère sur les correspondances
for match_id, start, end in matcher(doc):
    # Crée un Span avec le libellée pour "GPE"
    span = ____(____, ____, ____, label=____)

    # Actualise doc.ents avec l'ajout du span
    doc.ents = list(doc.ents) + [____]

    # Obtiens la tête de la racine du span
    span_root_head = ____.____.____
    # Affiche le texte de la tête de la racine et le texte du span
    print(span_root_head.____, "-->", span.text)

# Affiche les entités dans le document
print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "GPE"])
