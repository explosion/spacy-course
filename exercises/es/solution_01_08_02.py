import spacy

nlp = spacy.load("es_core_news_sm")

text = (
    "De acuerdo con la revista Fortune, Apple fue la empresa "
    "más admirada en el mundo entre 2008 y 2012."
)

# Procesa el texto
doc = nlp(text)

# Itera sobre las entidades predichas
for ent in doc.ents:
    # Imprime en pantalla el texto de la entidad y su label
    print(ent.text, ent.label_)
