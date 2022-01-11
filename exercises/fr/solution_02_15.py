import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
import json

with open("exercises/fr/countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())
with open("exercises/fr/country_text.txt", encoding="utf8") as f:
    TEXT = f.read()

nlp = spacy.load("fr_core_news_sm")
matcher = PhraseMatcher(nlp.vocab)
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", patterns)

# Crée un doc et réinitialise les entités existantess
doc = nlp(TEXT)
doc.ents = []

# Itère sur les correspondances
for match_id, start, end in matcher(doc):
    # Crée un Span avec le label pour "GPE"
    span = Span(doc, start, end, label="GPE")

    # Actualise doc.ents avec l'ajout du span
    doc.ents = list(doc.ents) + [span]

    # Obtiens la tête de la racine du span
    span_root_head = span.root.head
    # Affiche le texte de la tête de la racine et le texte du span
    print(span_root_head.text, "-->", span.text)

# Affiche les entités dans le document
print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "GPE"])
