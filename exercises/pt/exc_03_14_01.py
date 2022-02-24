import json
import spacy

nlp = spacy.load("pt_core_news_sm")

with open("exercises/pt/tweets.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

# Processar os textos e imprimir os adjetivos
for text in TEXTS:
    doc = nlp(text)
    print([token.text for token in doc if token.pos_ == "ADJ"])
