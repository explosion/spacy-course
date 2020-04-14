def test():
    assert (
        person_hash == nlp.vocab.strings["PERSON"]
    ), "Did you assign the correct hash?"
    assert (
        'nlp.vocab.strings["PERSON"]' in __solution__
        or "nlp.vocab.strings['PERSON']" in __solution__
    )
    assert person_string == "PERSON", "Did you get the correct string?"
    assert (
        "nlp.vocab.strings[person_hash]" in __solution__
    ), "Did you get the string from the hash?"

    __msg__.good("Good job!")
