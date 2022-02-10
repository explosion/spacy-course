import spacy

nlp = spacy.load("pt_core_news_md")

doc1 = nlp("Eu quero comprar um livro novo")
doc2 = nlp("Preciso ler um livro")

# Obtenha a similiridade entre doc1 e doc2
similarity = ____.____(____)
print(similarity)
