def test():
    import spacy.matcher

    assert isinstance(
        matcher, spacy.matcher.Matcher
    ), "Are you initializing the matcher correctly?"
    assert (
        "Matcher(nlp.vocab)" in __solution__
    ), "Are you initializing the matcher correctly with the shared vocab?"
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
        pattern[0].get(key) == "iPhone" for key in ["text", "TEXT"]
    ), "Are you matching on the token text?"
    assert any(
        pattern[1].get(key) == "X" for key in ["text", "TEXT"]
    ), "Are you matching on the token text?"
    assert (
        'matcher.add("IPHONE_X_PATTERN"' in __solution__
    ), "Are you adding the match pattern correctly?"
    assert (
        "matches = matcher(doc)" in __solution__
    ), "Are you calling the matcher on the doc?"

    __msg__.good(
        "Well done! You successfully found one match: the tokens at doc[1:3] "
        'describing the span for "iPhone X".'
    )
