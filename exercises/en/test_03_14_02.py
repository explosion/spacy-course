def test():
    assert (
        "docs = list(nlp.pipe(TEXTS))" in __solution__
    ), "Are you using nlp.pipe wrapped in a list?"
    __msg__.good("Great work!")
