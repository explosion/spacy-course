def test():
    assert "token_texts" not in __solution__, "Did you remove the token_texts variable?"
    assert "pos_tags" not in __solution__, "Did you remove the pos_tags variable?"
    assert (
        "token.pos_ ==" in __solution__
    ), "Are you checking whether the token's part-of-speech tag is a proper noun?"
    assert (
        "token.i + 1" in __solution__ or "token.i+1" in __solution__
    ), "Are you using the token's index attribute to check the next token?"
    __msg__.good("Great work!")
