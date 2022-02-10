def test():
    assert gato_hash == nlp.vocab.strings["gato"], "Você atribuiu o código hash corretamente?"
    assert 'nlp.vocab.strings["gato"]' in __solution__, "Você selecionou a string corretamente?"
    assert gato_string == "gato", "Você selecionou a string corretamente?"
    assert (
        "nlp.vocab.strings[gato_hash]" in __solution__
    ), "Você obteve a string a partir do código hash?"

    __msg__.good("Ótimo trabalho!")
