def test():
    assert Token.has_extension(
        "reversed"
    ), "Did you register the extension on the token?"
    ext = Token.get_extension("reversed")
    assert ext[2] is not None, "Did you set the getter correctly?"
    assert (
        "getter=get_reversed" in __solution__
    ), "Did you assign get_reversed as the getter?"
    assert "token._.reversed" in __solution__, "Are you accessing the custom attribute?"

    __msg__.good("Good job! Let's set some more complex attributes.")
