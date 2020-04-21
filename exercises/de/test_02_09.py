def test():
    assert (
        'spacy.load("en_core_web_md")' in __solution__
    ), "Lädst du das mittelgroße Modell?"
    assert "doc[1].vector" in __solution__, "Greifst du auf den richtigen Vector zu?"
    __msg__.good(
        "Bravo! In der nächsten Übung wirst du spaCy benutzen, um mithilfe von "
        "Wortvektoren Ähnlichkeiten von Dokumenten, Spans und Tokens zu berechnen."
    )
