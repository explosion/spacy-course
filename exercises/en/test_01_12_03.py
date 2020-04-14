def test():
    assert (
        len(pattern) == 3
    ), "The pattern should describe three tokens (three dictionaries)."
    assert (
        isinstance(pattern[0], dict)
        and isinstance(pattern[1], dict)
        and isinstance(pattern[2], dict)
    ), "Each entry in a pattern should be a dictionary."
    assert (
        len(pattern[0]) == 1 and len(pattern[1]) == 1
    ), "The first two pattern entries should have only one key."
    assert len(pattern[2]) == 2, "The third pattern entry should have two keys."
    assert any(
        pattern[0].get(key) == "ADJ" for key in ["pos", "POS"]
    ), "Are you matching on the first token's part-of-speech tag with the correct label?"
    assert any(
        pattern[1].get(key) == "NOUN" for key in ["pos", "POS"]
    ), "Are you matching on the second token's part-of-speech tag with the correct label?"
    assert any(
        pattern[2].get(key) == "NOUN" for key in ["pos", "POS"]
    ), "Are you matching on the third token's part-of-speech tag with the correct label?"
    assert (
        pattern[2].get("OP") == "?"
    ), "Are you using the correct operator for the third token?"

    __msg__.good(
        "Great work – those were some pretty complex patterns! Let's move on "
        "to the next chapter and take a look at how to use spaCy for more "
        "advanced text analysis."
    )
