def test():
    assert gato_hash == nlp.vocab.strings["gato"], "¿Asignaste el hash correcto?"
    assert 'nlp.vocab.strings["gato"]' in __solution__
    assert gato_string == "gato", "¿Obtuviste el string correcto?"
    assert (
        "nlp.vocab.strings[gato_hash]" in __solution__
    ), "¿Obtuviste el string usando el hash?"

    __msg__.good("¡Muy buen trabajo!")
