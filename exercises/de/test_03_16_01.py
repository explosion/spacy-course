def test():
    assert (
        "doc = nlp.make_doc(text)" in __solution__
        or "doc = nlp.tokenizer(text)" in __solution__
    ), "Verwendest du tatsächlich nur den Tokenizer?"

    __msg__.good("Sehr schön!")
