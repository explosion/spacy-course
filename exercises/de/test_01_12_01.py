def test():
    assert (
        len(pattern) == 2
    ), "Das Pattern sollte zwei Tokens beschreiben (zwei Dictionaries)."
    assert isinstance(pattern[0], dict) and isinstance(
        pattern[1], dict
    ), "Jeder Eintrag im Pattern sollte ein Dictionary sein."
    assert (
        len(pattern[0]) == 1 and len(pattern[1]) == 1
    ), "Jeder Eintrag im Pattern sollte nur einen Schlüssel haben."
    assert any(
        pattern[0].get(key) == "iOS" for key in ["text", "TEXT"]
    ), "Suchst du nach dem Text des ersten Tokens?"
    assert any(
        pattern[1].get(key) == True for key in ["is_digit", "IS_DIGIT"]
    ), "Suchst du nach dem Attribut is_digit des zweiten Tokens?"

    __msg__.good("Sehr gut!")
