def test():
    assert cat_hash == nlp.vocab.strings["cat"], "¿Asignaste el hash correcto?"
    assert (
        'nlp.vocab.strings["cat"]' in __solution__
        or "nlp.vocab.strings['cat']" in __solution__
    )
    assert cat_string == "cat", "¿Obtuviste el string correcto?"
    assert (
        "nlp.vocab.strings[cat_hash]" in __solution__
    ), "¿Obtuviste el string usando el hash?"

    __msg__.good("¡Gran trabajo!")
