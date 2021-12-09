def test():
    assert (
        "for doc in nlp.pipe(TEXTS)" in __solution__
    ), "Você está iterando nos docs retornados em nlp.pipe?"
    __msg__.good("Bom!")
