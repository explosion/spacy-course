def test():
    assert (
        "docs = list(nlp.pipe(TEXTS))" in __solution__
    ), "Verwendest du nlp.pipe in einer Liste?"
    __msg__.good("Gute Arbeit!")
