import spacy

# Carga el modelo "es_core_news_sm"
nlp = spacy.load("es_core_news_sm")

text = (
    "De acuerdo con la revista Fortune, Apple fue la empresa "
    "más admirada en el mundo entre 2008 y 2012."
)

# Procesa el texto
doc = nlp(text)

# Imprime en pantalla el texto del documento
print(doc.text)
