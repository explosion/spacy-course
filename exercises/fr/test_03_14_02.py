def test():
    assert (
        "docs = list(nlp.pipe(TEXTS))" in __solution__
    ), "Utilises-tu nlp.pipe enveloppé dans une liste ?"
    __msg__.good("Super boulot !")
