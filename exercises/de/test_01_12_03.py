def test():
    assert (
        len(pattern) == 3
    ), "Das Pattern sollte drei Tokens beschreiben (drei Dictionaries)."
    assert (
        isinstance(pattern[0], dict)
        and isinstance(pattern[1], dict)
        and isinstance(pattern[2], dict)
    ), "Jeder Eintrag im Pattern sollte ein Dictionary sein."
    assert (
        len(pattern[0]) == 1
    ), "Der erste Eintrag im Pattern sollte nur einen Schlüssel haben."
    assert (
        len(pattern[1]) == 2
    ), "Der zweite Eintrag im Pattern sollte zwei Schlüssel haben."
    assert (
        len(pattern[2]) == 1
    ), "Der dritte Eintrag im Pattern sollte nur einen Schlüssel haben."
    assert any(
        pattern[0].get(key) == "ADJ" for key in ["pos", "POS"]
    ), "Suchst du nach der Wortart des ersten Tokens und benutzt du das korrekte Label?"
    assert any(
        pattern[1].get(key) == "ADJ" for key in ["pos", "POS"]
    ), "Suchst du nach der Wortart des zweiten Tokens und benutzt du das korrekte Label?"
    assert (
        pattern[1].get("OP") == "?"
    ), "Verwendest du den korrekten Operator für den zweiten Token?"

    assert any(
        pattern[2].get(key) == "NOUN" for key in ["pos", "POS"]
    ), "Suchst du nach der Wortart des dritten Tokens und benutzt du das korrekte Label?"
    __msg__.good(
        "Gut gemacht – da waren echt ein paar komplexe Patterns dabei! Lass uns "
        "mit dem nächsten Kapitel weitermachen und anschauen, wie wir spaCy für "
        "fortgeschrittene Textanalyse verwenden können."
    )
