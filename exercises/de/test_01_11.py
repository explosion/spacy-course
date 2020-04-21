def test():
    import spacy.matcher

    assert isinstance(
        matcher, spacy.matcher.Matcher
    ), "Initialisierst du den Matcher richtig?"
    assert (
        "Matcher(nlp.vocab)" in __solution__
    ), "Initialisierst du den Matcher korrekt mit dem gemeinsamen Vokabular?"
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
        pattern[0].get(key) == "iPhone" for key in ["text", "TEXT"]
    ), "Suchst du nach dem Text des ersten Tokens?"
    assert any(
        pattern[1].get(key) == "X" for key in ["text", "TEXT"]
    ), "Suchst du nach dem Text des zweiten Tokens?"
    assert (
        'matcher.add("IPHONE_X_PATTERN"' in __solution__
    ), "Hast du das Pattern korrekt zum Matcher hinzugefügt?"
    assert (
        "matches = matcher(doc)" in __solution__
    ), "Rufst du den Matcher mit dem Doc als Argument auf?"

    __msg__.good(
        "Gut gemacht! Du hast erfolgreich ein Resultat gefunden: die Tokens an "
        'Position doc[2:4] beschreiben die Span "iPhone X".'
    )
