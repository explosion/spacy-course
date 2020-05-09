def test():
    assert (
        "for doc in nlp.pipe(TEXTS)" in __solution__
    ), "¿Estás iterando sobre los docs que fueron devueltos usando <code>yield<code> por nlp.pipe?"
    __msg__.good("¡Bien!")
