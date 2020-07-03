def test():
    assert person_hash == nlp.vocab.strings["PER"], "¿Asignaste el hash correcto?"
    assert 'nlp.vocab.strings["PER"]' in __solution__
    assert person_string == "PER", "¿Obtuviste el string correcto?"
    assert (
        "nlp.vocab.strings[person_hash]" in __solution__
    ), "¿Obtuviste el string usando el hash?"

    __msg__.good("¡Buen trabajo!")
