import spacy

nlp = spacy.load("de_core_news_sm")
doc = nlp("Berlin gefällt mir sehr gut")

# Finde alle Tokens und Wortarten
token_texts = [token.text for token in doc]
pos_tags = [token.pos_ for token in doc]

for index, pos in enumerate(pos_tags):
    # Teste, ob der aktuelle Token ein Eigenname ist
    if pos == "PROPN":
        # Teste, ob der nächste Token ein Verb ist
        if pos_tags[index + 1] == "VERB":
            result = token_texts[index]
            print("Eigenname vor Verb gefunden:", result)
