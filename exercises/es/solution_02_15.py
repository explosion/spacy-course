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

# Crea un doc y restablece las entidades existentes
doc = nlp(TEXT)
doc.ents = []

# Itera sobre los resultados
for match_id, start, end in matcher(doc):
    # Crea un Span con el label para "GPE"
    span = Span(doc, start, end, label="GPE")

    # Sobrescribe el doc.ents y añade el span
    doc.ents = list(doc.ents) + [span]

    # Obtén el token central de la raíz del span
    span_root_head = span.root.head
    # Imprime en pantalla el texto del token central de la raíz del span y el texto del span
    print(span_root_head.text, "-->", span.text)

# Imprime en pantalla las entidades del documento
print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "GPE"])
