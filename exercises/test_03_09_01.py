def test():
    assert Token.has_extension(
        "is_country"
    ), "Did you register the extension on the token?"
    ext = Token.get_extension("is_country")
    assert ext[0] == False, "Did you set the default value correctly?"
    assert (
        "doc[3]._.is_country = True" in __solution__
    ), "Did you change the value for the right token?"
    assert (
        "print([(token.text, token._.is_country)" in __solution__
    ), "Are you printing the right token attributes?"

    __msg__.good("Well done!")
