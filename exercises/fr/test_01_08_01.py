def test():
    assert (
        "token_text = token.text" in __solution__
    ), "Are you getting the token's text correctly?"
    assert (
        "token_pos = token.pos_" in __solution__
    ), "Are you getting the token's part-of-speech tag correctly? Remember to use the underscore attribute."
    assert (
        "token_dep = token.dep_" in __solution__
    ), "Are you getting the token's dependency label correctly? Remember to use the underscore attribute."
    __msg__.good("Perfect!")
