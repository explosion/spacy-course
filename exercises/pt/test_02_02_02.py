def test():
    assert (
        person_hash == nlp.vocab.strings["PERSON"]
    ), "Você atribuiu o código hash corretamente?"
    assert (
        'nlp.vocab.strings["PERSON"]' in __solution__
    ), "Você atribuiu o código hash corretamente?"
    assert person_string == "PERSON", "Você selecionou a string corretamente?"
    assert (
        "nlp.vocab.strings[person_hash]" in __solution__
    ), "Você obteve a string a partir do código hash?"

    __msg__.good("Good job!")
