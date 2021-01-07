def test():
    assert cat_hash == nlp.vocab.strings["cat"], "Você atribuiu o código hash corretamente?"
    assert 'nlp.vocab.strings["cat"]' in __solution__, "Você selecionou a string corretamente?"
    assert cat_string == "cat", "Você selecionou a string corretamente?"
    assert (
        "nlp.vocab.strings[cat_hash]" in __solution__
    ), "Você obteve a string a partir do código hash?"

    __msg__.good("Ótimo trabalho!")
