from spacy.lang.es import Spanish

nlp = Spanish()

# Procesa el texto
doc = nlp(
    "En 1990, más del 60% de las personas en Asia del Este se encontraban "
    "en extrema pobreza. Ahora, menos del 4% lo están."
)

# Itera sobre los tokens en el doc
for token in doc:
    # Revisa si el token parece un número
    if ____.____:
        # Obtén el próximo token en el documento
        next_token = ____[____]
        # Revisa si el texto del siguiente token es igual a '%'
        if next_token.____ == "%":
            print("Porcentaje encontrado::", token.text)
