import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Berlin is a nice city")

# Selecionar todos os tokens e as classes gramaticais
token_texts = [token.text for token in doc]
pos_tags = [token.pos_ for token in doc]

for index, pos in enumerate(pos_tags):
    # Verifica se o token atual é um substantivo próprio
    if pos == "PROPN":
        # Verifica se o próximo token é um verbo
        if pos_tags[index + 1] == "VERB":
            result = token_texts[index]
            print("Found proper noun before a verb:", result)
