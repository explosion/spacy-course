def test():
    assert "token_texts" not in __solution__, "Did you remove the token_texts variable?"
    assert "pos_tags" not in __solution__, "Did you remove the pos_tags variable?"
    assert (
        "token.pos_ ==" in __solution__
    ), "Are you checking whether the token's part-of-speech tag is a proper noun?"
    assert (
        "token.i + 1" in __solution__ or "1 + token.i" in __solution__
    ), "Are you using the token's index attribute to check the next token?"
    __msg__.good(
        "Great work! While the solution here works fine for the given example, "
        "there are still things that can be improved. If the doc ends with a "
        "proper noun, doc[token.i + 1] will fail. To make sure the code "
        "generalizes, you should first check if token.i + 1 < len(doc)."
    )
