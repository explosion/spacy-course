import spacy

nlp = spacy.load("es_core_news_md")

doc1 = nlp("Es un cálido día de verano")
doc2 = nlp("Hay sol afuera")

# Obtén la similitud entre el doc1 y el doc2
similarity = ____.____(____)
print(similarity)
