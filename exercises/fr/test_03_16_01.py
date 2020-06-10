def test():
    assert (
        "doc = nlp.make_doc(text)" in __solution__
        or "doc = nlp.tokenizer(text)" in __solution__
    ), "Are you only tokenizing the text?"

    __msg__.good("Nicely done!")
