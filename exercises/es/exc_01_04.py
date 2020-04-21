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
    if ____.____:
        # Obtén el próximo token en el documento
        next_token = ____[____]
        # Revisa si el texto del siguiente token es igual a '%'
        if next_token.____ == "%":
            print("Percentage found:", token.text)
