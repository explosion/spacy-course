def test():
    assert len(pattern1) == 2, "pattern1 should describe two tokens."
    assert len(pattern2) == 2, "pattern2 should describe two tokens."
    assert (
        len(pattern1[0]) == 1
    ), "The first token of pattern1 only needs one attribute."
    assert any(
        pattern1[0].get(l) == "iphone" for l in ("LOWER", "lower")
    ), "The first token of pattern1 should match lowercase 'iphone'."
    assert (
        len(pattern1[1]) == 1
    ), "The second token of pattern1 only needs one attribute."
    assert any(
        pattern1[1].get(l) == "x" for l in ("LOWER", "lower")
    ), "The second token of pattern1 should match lowercase 'x'."
    assert (
        len(pattern2[0]) == 1
    ), "The first token of pattern2 only needs one attribute."
    assert any(
        pattern2[0].get(l) == "iphone" for l in ("LOWER", "lower")
    ), "The first token of pattern2 should match lowercase 'iphone'."
    assert (
        len(pattern2[1]) == 2
    ), "The second token of pattern2 should have two attributes."
    assert any(
        pattern2[1].get(l) == True for l in ("IS_DIGIT", "is_digit")
    ), "The second token of pattern2 should match a digit."
    assert any(
        pattern2[1].get(l) == "?" for l in ("OP", "op")
    ), "Are you using the correct operator in the second token of pattern2?"

    __msg__.good(
        "Nice! Now let's use those patterns to quickly bootstrap some training "
        "data for our model."
    )
