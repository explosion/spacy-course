import spacy

nlp = spacy.load("es_core_news_md")

doc = nlp(
    "Estuvimos en un restaurante genial. Luego, fuimos a un bar muy divertido."
)

# Crea los spans para "restaurante genial" y "bar muy divertido"
span1 = doc[3:5]
span2 = doc[11:14]

# Obtén la similitud entre los dos spans
similarity = span1.similarity(span2)
print(similarity)
