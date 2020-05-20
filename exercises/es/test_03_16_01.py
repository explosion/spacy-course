def test():
    assert (
        "doc = nlp.make_doc(text)" in __solution__
        or "doc = nlp.tokenizer(text)" in __solution__
    ), "¿Solo estás convirtiendo el texto en tokens?"

    __msg__.good("¡Bien hecho!")
