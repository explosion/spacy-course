def test():
    assert (
        doc.text == "Ich mag niedliche Katzen und Faultiere."
    ), "Bist du dir sicher, dass du den Text korrekt verarbeitet hast?"
    assert erster_token == doc[0], "Bist du dir sicher, dass du den ersten Token ausgewählt hast?"
    assert "print(erster_token.text)" in __solution__, "Druckst du den Text des Tokens?"
    __msg__.good("Sehr schön!")
