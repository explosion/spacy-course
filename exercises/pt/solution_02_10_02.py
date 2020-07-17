import spacy

nlp = spacy.load("en_core_web_md")

doc = nlp("TV and books")
token1, token2 = doc[0], doc[2]

# Obtenha a similaridade dos tokens "TV" e "books"
similarity = token1.similarity(token2)
print(similarity)
