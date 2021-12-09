def test():
    assert (
        "if token.like_num" in __solution__
    ), "Are you checking the token's like_num attribute?"
    assert (
        'next_token.text == "%"' in __solution__
    ), "Are you checking whether the next token's text is a percent sign?"
    assert (
        next_token.text == "%"
    ), "Are you checking whether the next token's text is a percent sign?"
    assert (
        "token.i + 1" in __solution__ or "1 + token.i" in __solution__
    ), "Are you using the token's index attribute?"

    __msg__.good(
        "Well done! As you can see, you can do a lot of very powerful "
        "analyses using the tokens and their attributes."
    )
