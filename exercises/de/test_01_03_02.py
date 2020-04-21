def test():
    assert (
        doc.text == "Ich mag niedliche Katzen und Faultiere."
    ), "Bist du dir sicher, dass du den Text korrekt verarbeitet hast?"
    assert (
        niedliche_katzen == doc[2:4]
    ), "Bist du dir sicher, dass du die korrekte Span für niedliche_katzen ausgewählt hast?"
    assert (
        niedliche_katzen_und_faultiere == doc[2:6]
    ), "Bist du dir sicher, dass du die korrekte Span für niedliche_katzen_und_faultiere ausgewählt hast?"
    __msg__.good("Gut gemacht!")
