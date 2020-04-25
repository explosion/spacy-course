import spacy

# Carga el modelo "en_core_web_sm"
nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Procesa el texto
doc = nlp(text)

# Imprime en pantalla el texto del documento
print(doc.text)
