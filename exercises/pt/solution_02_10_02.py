import spacy

nlp = spacy.load("pt_core_news_md")

doc = nlp("Televisão e livro")
token1, token2 = doc[0], doc[2]

# Obtenha a similaridade dos tokens "TV" e "books"
similarity = token1.similarity(token2)
print(similarity)
