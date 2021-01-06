def test():
    assert (
        "docs = list(nlp.pipe(TEXTS))" in __solution__
    ), "Você está usando nlp.pipe envolvido em uma lista (list)?"
    __msg__.good("Bom trabalho!")
