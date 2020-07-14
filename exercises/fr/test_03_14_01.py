def test():
    assert (
        "for doc in nlp.pipe(TEXTS)" in __solution__
    ), "Itères-tu sur les docs générés par nlp.pipe ?"
    __msg__.good("Joli !")
