def test():
    assert (
        "for doc in nlp.pipe(TEXTS)" in __solution__
    ), "Are you iterating over docs yielded by nlp.pipe?"
    __msg__.good("Nice!")
