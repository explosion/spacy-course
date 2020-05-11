def test():
    assert (
        "docs = list(nlp.pipe(TEXTS))" in __solution__
    ), "¿Estás usando nlp.pipe envuelto en una lista?"
    __msg__.good("¡Muy buen trabajo!")
