def test():
    assert (
        "doc = nlp.make_doc(text)" in __solution__
        or "doc = nlp.tokenizer(text)" in __solution__
    ), "Você está apenas toquenizando o texto?"

    __msg__.good("Muito bom!")
