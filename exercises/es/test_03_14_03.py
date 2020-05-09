def test():
    assert (
        "patterns = list(nlp.pipe(people))" in __solution__
    ), "¿Estás usando nlp.pipe envuelto en una lista?"

    __msg__.good(
        "¡Buen trabajo! Ahora continuemos con un ejemplo práctico que usa nlp.pipe "
        "para procesar documentos con metadatos adicionales."
    )
