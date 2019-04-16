def test():
    assert (
        "patterns = list(nlp.pipe(people))" in __solution__
    ), "Are you using nlp.pipe wrapped in a list?"

    __msg__.good(
        "Good job! Let's move on to a practical example that uses `nlp.pipe` "
        "to process documents with additional meta data."
    )
