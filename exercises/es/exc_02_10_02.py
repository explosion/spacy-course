import spacy

nlp = spacy.load("en_core_web_md")

doc = nlp("TV and books")
token1, token2 = doc[0], doc[2]

# Obtén la similitud entre los tokens "TV" y "books"
similarity = ____.____(____)
print(similarity)
