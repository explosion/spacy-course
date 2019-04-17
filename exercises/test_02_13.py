def test():
    assert (
        len(pattern1) == 2
    ), "The number of tokens in pattern1 doesn't match the real number of tokens in the string."
    assert (
        len(pattern2) == 4
    ), "The number of tokens in pattern2 doesn't match the real number of tokens in the string."
    # Pattern 1 validation
    assert (
        len(pattern1[0]) == 1
    ), "The first token of pattern1 should include one attribute."
    assert any(
        pattern1[0].get(attr) == "amazon" for attr in ("lower", "LOWER")
    ), "Check the attribute and value of the first token in pattern1."
    assert (
        len(pattern1[1]) == 2
    ), "The second token of pattern1 should include two attributes."
    assert any(
        pattern1[1].get(attr) == True for attr in ("is_title", "IS_TITLE")
    ), "Check the attributes and values of the second token in pattern1."
    assert any(
        pattern1[1].get(attr) == "PROPN" for attr in ("pos", "POS")
    ), "Check the attributes and values of the second token in pattern1."

    # Pattern 2 validation
    assert any(
        pattern2[0].get(attr) == "ad" for attr in ("lower", "LOWER")
    ), "Check the attribute and value of the first token in pattern2."
    assert any(
        pattern2[2].get(attr) == "free" for attr in ("lower", "LOWER")
    ), "Check the attribute and value of the third token in pattern2."
    assert any(
        pattern2[3].get(attr) == "NOUN" for attr in ("pos", "POS")
    ), "Check the attribute and value of the fourth token in pattern2."
    assert len(matcher(doc)) == 6, "Incorrect number of matches – expected 6."

    __msg__.good(
        "Well done! For the token `-`, you can match on the attribute "
        "`TEXT`, `LOWER` or even `SHAPE`. All of those are correct. As you "
        "can see, paying close attention to the tokenization is very "
        "important when working with the token-based `Matcher`. Sometimes "
        "it's much easier to just match exact strings instead and use the "
        "`PhraseMatcher`, which we'll get to in the next exercise."
    )
