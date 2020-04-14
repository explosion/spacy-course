def test():
    assert (
        "from spacy.tokens import Doc" in __solution__
    ), "Are you importing the Doc class correctly?"
    assert (
        len(spaces) == 5
    ), "Looks like the number of spaces doesn't match the number of words."
    assert all(isinstance(s, bool) for s in spaces), "The spaces need to be booleans."
    assert [int(s) for s in spaces] == [0, 1, 1, 0, 0], "Are the spaces correct?"
    assert doc.text == "Go, get started!", "Are you sure you created the Doc correctly?"
    __msg__.good("Nice!")
