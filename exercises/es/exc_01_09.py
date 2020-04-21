import spacy

nlp = spacy.load("en_core_web_sm")

text = "New iPhone X release date leaked as Apple reveals pre-orders by mistake"

# Procesa el texto
doc = ____

# Itera sobre las entidades
for ____ in ____.____:
    # Imprime en pantalla el texto de la entidad y su label
    print(____.____, ____.____)

# Obtén el span para "iPhone X"
iphone_x = ____

# Imprime en pantalla el texto del span
print("Missing entity:", iphone_x.text)
