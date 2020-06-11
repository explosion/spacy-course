import spacy

nlp = spacy.load("es_core_news_sm")

text = (
    "Los Olímpicos de Tokio 2020 son la inspiración para la nueva "
    "colección de zapatillas adidas ZX."
)

# Procesa el texto
doc = ____

# Itera sobre las entidades
for ____ in ____.____:
    # Imprime en pantalla el texto de la entidad y su label
    print(____.____, ____.____)

# Obtén el span para "adidas ZX"
adidas_zx = ____

# Imprime en pantalla el texto del span
print("Entidad faltante:", adidas_zx.text)
