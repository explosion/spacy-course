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

# Criar um doc e reiniciar (zerar) as entidades existentes
doc = nlp(TEXT)
doc.ents = []

# Iterar nos resultados do combinador 
for match_id, start, end in matcher(doc):
    # Criar uma partição Span com o marcador para "GPE"
    span = Span(doc, start, end, label="GPE")

    # Atualizar doc.ents com essa partição
    doc.ents = list(doc.ents) + [span]

    # Identificar o token inicial da partição
    span_root_head = span.root.head
    # Imprimir o texto to token inicial da partição e o texto da partição
    print(span_root_head.text, "-->", span.text)

# Imprimir as entidades do documento
print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "GPE"])
