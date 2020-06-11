import spacy

nlp = spacy.load("es_core_news_md")

doc = nlp("TV y libros")
token1, token2 = doc[0], doc[2]

# Obtén la similitud entre los tokens "TV" y "libros"
similarity = token1.similarity(token2)
print(similarity)
