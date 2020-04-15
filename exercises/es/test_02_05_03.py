def test():
    assert (
        "from spacy.tokens import Doc" in __solution__
    ), "Are you importing the Doc class correctly?"
    assert len(words) == 5, "Looks like you have an incorrect number of words."
    assert len(spaces) == 5, "Looks like you have an incorrect number of spaces."
    assert words == ["Oh", ",", "really", "?", "!"], "Double-check the words!"
    assert all(isinstance(s, bool) for s in spaces), "The spaces need to be booleans."
    assert [int(s) for s in spaces] == [0, 1, 0, 0, 0], "Are the spaces correct?"
    assert doc.text == "Oh, really?!", "Are you sure you created the Doc correctly?"
    __msg__.good("Nice work! Next, let's create some entities.")
