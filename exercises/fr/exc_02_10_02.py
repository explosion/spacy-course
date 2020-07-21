import spacy

nlp = spacy.load("fr_core_news_md")

doc = nlp("télé et livres")
token1, token2 = doc[0], doc[2]

# Obtiens la similarité entre les tokens "télé" et "livres"
similarity = ____.____(____)
print(similarity)
