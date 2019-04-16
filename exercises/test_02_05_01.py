def test():
    assert (
        "from spacy.tokens import Doc" in __solution__
    ), "Are you importing the Doc class correctly?"
    assert doc.text == "spaCy is cool!", "Are you sure you created the Doc correctly?"
    __msg__.good("Well done!")
