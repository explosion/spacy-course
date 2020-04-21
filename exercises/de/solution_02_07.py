import spacy

nlp = spacy.load("de_core_news_sm")
doc = nlp("Berlin gefällt mir sehr gut")

# Iteriere über die Tokens
for token in doc:
    # Teste, ob der aktuelle Token ein Eigenname ist
    if token.pos_ == "PROPN":
        # Teste, ob der nächste Token ein Verb ist
        if doc[token.i + 1].pos_ == "VERB":
            print("Eigenname vor Verb gefunden:", token.text)
