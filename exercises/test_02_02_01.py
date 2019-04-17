def test():
    assert cat_hash == nlp.vocab.strings["cat"], "Did you assign the correct hash?"
    assert (
        'nlp.vocab.strings["cat"]' in __solution__
        or "nlp.vocab.strings['cat']" in __solution__
    )
    assert cat_string == "cat", "Did you get the correct string?"
    assert (
        "nlp.vocab.strings[cat_hash]" in __solution__
    ), "Did you get the string from the hash?"

    __msg__.good("Great work!")
