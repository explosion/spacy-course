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
        pattern[0].get(key) == "download" for key in ["lemma", "LEMMA"]
    ), "Suchst du nach dem Lemma des ersten Tokens?"
    assert any(
        pattern[1].get(key) == "PROPN" for key in ["pos", "POS"]
    ), "Suchst du nach der Wortart des zweiten Tokens, und benutzt du das korrekte Label für Eiggennamen (proper noun)?"

    __msg__.good("Gute Arbeit!")
