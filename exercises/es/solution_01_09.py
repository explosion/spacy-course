import spacy

nlp = spacy.load("en_core_web_sm")

text = "New iPhone X release date leaked as Apple reveals pre-orders by mistake"

# Procesa el texto
doc = nlp(text)

# Itera sobre las entidades
for ent in doc.ents:
    # Imprime en pantalla el texto de la entidad y su label
    print(ent.text, ent.label_)

# Obtén el span para "iPhone X"
iphone_x = doc[1:3]

# Imprime en pantalla el texto del span
print("Missing entity:", iphone_x.text)
