def test():
    assert (
        len(pattern) == 2
    ), "The pattern should describe two tokens (two dictionaries)."
    assert isinstance(pattern[0], dict) and isinstance(
        pattern[1], dict
    ), "Each entry in a pattern should be a dictionary."
    assert (
        len(pattern[0]) == 1 and len(pattern[1]) == 1
    ), "Each entry in the pattern should have only one key."
    assert any(
        pattern[0].get(key) == "download" for key in ["lemma", "LEMMA"]
    ), "Are you matching on the first token's lemma?"
    assert any(
        pattern[1].get(key) == "PROPN" for key in ["pos", "POS"]
    ), "Are you matching on the second token's part-of-speech tag and using the right label for proper noun?"

    __msg__.good("Good job!")
