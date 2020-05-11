def test():
    assert (
        person_hash == nlp.vocab.strings["PERSON"]
    ), "¿Asignaste el hash correcto?"
    assert (
        'nlp.vocab.strings["PERSON"]' in __solution__
        or "nlp.vocab.strings['PERSON']" in __solution__
    )
    assert person_string == "PERSON", "¿Obtuviste el string correcto?"
    assert (
        "nlp.vocab.strings[person_hash]" in __solution__
    ), "¿Obtuviste el string usando el hash?"

    __msg__.good("¡Buen trabajo!")
