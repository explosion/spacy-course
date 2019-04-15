def test():
    assert (
        doc.text == "I like tree kangaroos and narwhals."
    ), "Are you sure you processed the text correctly?"
    assert first_token == doc[0], "Are you sure you selected the first token?"
    assert "print(first_token.____)" in __solution__
    __msg__.good("Nicely done!")
