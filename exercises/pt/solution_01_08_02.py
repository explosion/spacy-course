import spacy

nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Processar o texto the text
doc = nlp(text)

# Iterar nas entidades previstas
for ent in doc.ents:
    # Imprimir o texto e a etiqueta da entidade
    print(ent.text, ent.label_)
