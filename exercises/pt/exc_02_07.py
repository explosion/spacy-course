import spacy

nlp = spacy.load("pt_core_news_sm")
doc = nlp("Berlin parece ser uma cidade bonita.")

# Iterar nos tokens
for token in doc:
    # Verifica se o token atual é um substantivo próprio.
    if token.pos_ == "PROPN":
        # Verifica se o próximo token é um verbo
        if doc[token.i + 1].pos_ == "VERB":
            print("Found proper noun before a verb:", token.text)
