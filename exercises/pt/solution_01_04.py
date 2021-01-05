from spacy.lang.en import English

nlp = English()

# Processar o texto
doc = nlp(
    "In 1990, more than 60% of people in East Asia were in extreme poverty. "
    "Now less than 4% are."
)

# Iterar os tokens de um documento doc
for token in doc:
    # Checar se o token é composto por algarismos numéricos
    if token.like_num:
        # Selecionar o próximo token do documento
        next_token = doc[token.i + 1]
        # Checar se o texto do proximo token é igual a "%"
        if next_token.text == "%":
            print("Percentage found:", token.text)
