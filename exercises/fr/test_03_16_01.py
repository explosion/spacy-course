def test():
    assert (
        "doc = nlp.make_doc(text)" in __solution__
        or "doc = nlp.tokenizer(text)" in __solution__
    ), "Est-ce que tu tokenises seulement le texte ?"

    __msg__.good("Bien joué !")
