import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
import json

with open("exercises/pt/countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())
with open("exercises/pt/country_text.txt", encoding="utf8") as f:
    TEXT = f.read()

nlp = spacy.load("pt_core_news_sm")
matcher = PhraseMatcher(nlp.vocab)
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", patterns)

# Criar um doc e reiniciar (zerar) as entidades existentes
doc = nlp(TEXT)
doc.ents = []

# Iterar nos resultados do combinador
for match_id, start, end in matcher(doc):
    # Criar uma partição Span com o marcador para "GPE"
    span = ____(____, ____, ____, label=____)

    # Atualizar doc.ents com essa partição
    doc.ents = list(doc.ents) + [____]

    # Identificar o token inicial da partição
    span_root_head = ____.____.____
    # Imprimir o texto to token inicial da partição e o texto da partição
    print(span_root_head.____, "-->", span.text)

# Imprimir as entidades do documento
print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "GPE"])
