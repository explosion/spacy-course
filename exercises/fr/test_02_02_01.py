def test():
    assert cat_hash == nlp.vocab.strings["cat"], "As-tu indiqué la bonne chaine pour obtenir le hash?"
    assert 'nlp.vocab.strings["cat"]' in __solution__, "As-tu indiqué la bonne chaine ?"
    assert cat_string == "cat", "As-tu indiqué la bonne chaine ?"
    assert (
        "nlp.vocab.strings[cat_hash]" in __solution__
    ), "As-tu indiqué le hash pour obtenir la chaine ?"

    __msg__.good("Bien joué !")
