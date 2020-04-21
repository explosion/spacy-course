def test():
    assert (
        "if token.like_num" in __solution__
    ), "Benutzt du das Token-Attribut like_num?"
    assert (
        'next_token.text == "%"' in __solution__
    ), "Testest du, ob der Text des nächsten Tokens ein Prozentzeichen ist?"
    assert (
        next_token.text == "%"
    ), "Testest du, ob der Text des nächsten Tokens ein Prozentzeichen ist?"

    __msg__.good(
        "Bravo! Wie du siehst, kann man Tokens und ihren Attributen für sehr "
        "aufschlussreiche Analysen verwenden."
    )
