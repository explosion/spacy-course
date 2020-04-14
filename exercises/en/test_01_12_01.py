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
        pattern[0].get(key) == "iOS" for key in ["text", "TEXT"]
    ), "Are you matching on the first token's text?"
    assert any(
        pattern[1].get(key) == True for key in ["is_digit", "IS_DIGIT"]
    ), "Are you matching on the second token's is_digit attribute?"

    __msg__.good("Well done!")
