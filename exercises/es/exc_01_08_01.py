import spacy

nlp = spacy.load("es_core_news_sm")

text = (
    "De acuerdo con la revista global de negocios Fortune, Apple fue "
    "la empresa más admirada en el mundo entre 2008 y 2012."
)

# Procesa el texto
doc = ____

for token in doc:
    # Obtén el texto del token, el part-of-speech tag y el dependency label
    token_text = ____.____
    token_pos = ____.____
    token_dep = ____.____
    # Esto es solo por formato
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")
