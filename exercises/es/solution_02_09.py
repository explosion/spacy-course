import spacy

# Carga el modelo en_core_web_md
nlp = spacy.load("en_core_web_md")

# Procesa un texto
doc = nlp("Two bananas in pyjamas")

# Obtén el vector para el token "bananas"
bananas_vector = doc[1].vector
print(bananas_vector)
