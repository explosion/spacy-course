import spacy

nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Procesa el texto
doc = nlp(text)

# Itera sobre las entidades predichas
for ent in doc.ents:
    # Imprime en pantalla el texto de la entidad y su label
    print(ent.text, ent.label_)
