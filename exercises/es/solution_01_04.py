from spacy.lang.en import English

nlp = English()

# Procesa el texto
doc = nlp(
    "In 1990, more than 60% of people in East Asia were in extreme poverty. "
    "Now less than 4% are."
)

# Itera sobre los tokens en el doc
for token in doc:
    # Revisa si el token parece un número
    if token.like_num:
        # Obtén el próximo token en el documento
        next_token = doc[token.i + 1]
        # Revisa si el texto del siguiente token es igual a '%'
        if next_token.text == "%":
            print("Percentage found:", token.text)
