import spacy

nlp = spacy.load("en_core_web_sm")

text = "Upcoming iPhone X release date leaked as Apple reveals pre-orders"

# Processar o texto
doc = nlp(text)

# Iterar nas entidades previstas
for ent in doc.ents:
    # Imprimir o texto e etiqueta (label) da entidade
    print(ent.text, ent.label_)

# Selecionar a partição para "iPhone X"
iphone_x = doc[1:3]

# Imprimir o texto da partição
print("Missing entity:", iphone_x.text)
