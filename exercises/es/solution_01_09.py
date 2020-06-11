import spacy

nlp = spacy.load("es_core_news_sm")

text = (
    "Los Olímpicos de Tokio 2020 son la inspiración para la nueva "
    "colección de zapatillas adidas ZX."
)

# Procesa el texto
doc = nlp(text)


# Itera sobre las entidades
for ent in doc.ents:
    # Imprime en pantalla el texto de la entidad y su label
    print(ent.text, ent.label_)

# Obtén el span para "adidas ZX"
adidas_zx = doc[14:16]

# Imprime en pantalla el texto del span
print("Entidad faltante:", adidas_zx.text)
