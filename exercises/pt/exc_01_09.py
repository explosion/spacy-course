import spacy

nlp = spacy.load("en_core_web_sm")

text = "Upcoming iPhone X release date leaked as Apple reveals pre-orders"

# Processar o texto
doc = ____

# Iterar nas entidades previstas
for ____ in ____.____:
    # Print the entity text and label
    print(____.____, ____.____)

# Selecionar a partição para "iPhone X"
iphone_x = ____

# Imprimir o texto da partição
print("Missing entity:", iphone_x.text)
