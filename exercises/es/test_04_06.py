def test():
    assert (
        'spacy.blank("es")' in __solution__
    ), "¿Creaste el modelo de español en blanco?"
    assert (
        len(nlp.pipe_names) == 1 and nlp.pipe_names[0] == "ner"
    ), "¿Añadiste el entity recognizer al pipeline?"
    assert (
        len(ner.labels) == 1 and ner.labels[0] == "ROPA"
    ), "¿Añadiste el label al entity recognizer?"

    __msg__.good(
        "¡Bien hecho! Ahora el pipeline está listo, así que vamos a comenzar a escribir el "
        "loop de entrenamiento."
    )
