import spacy

# Carga el modelo es_core_news_md
nlp = spacy.load("es_core_news_md")

# Procesa un texto
doc = nlp("Hoy hice pan de banano")

# Obtén el vector para el token "banano"
banano_vector = doc[4].vector
print(banano_vector)
