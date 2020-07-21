def test():
    assert (
        person_hash == nlp.vocab.strings["PER"]
    ), "As-tu indiqué la bonne chaine pour obtenir le hash ?"
    assert (
        'nlp.vocab.strings["PER"]' in __solution__
    ), "As-tu indiqué la bonne chaine pour obtenir le hash ?"
    assert person_string == "PER", "As-tu indiqué le bon hash pour obtenir la chaine ?"
    assert (
        "nlp.vocab.strings[person_hash]" in __solution__
    ), "As-tu indiqué le hash pour obtenir la chaine ?"

    __msg__.good("Bien joué !")
