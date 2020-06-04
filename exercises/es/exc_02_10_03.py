import spacy

nlp = spacy.load("es_core_news_md")

doc = nlp(
    "Estuvimos en un restaurante genial. Luego, fuimos a un bar muy divertido."
)

# Crea los spans para "restaurante genial" y "bar muy divertido"
span1 = ____
span2 = ____

# Obtén la similitud entre los dos spans
similarity = ____.____(____)
print(similarity)
