import spacy

# Carregue o fluxo de processamento pequeno do idioma inglês "en_core_web_sm"
nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Processe o texto
doc = nlp(text)

# Imprima o atributo texto do documento
print(doc.text)
