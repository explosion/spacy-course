def test():
    assert (
        "from spacy.tokens import Doc" in __solution__
    ), "Importierst du die Klasse Doc?"
    assert (
        len(spaces) == 5
    ), "Es sieht so aus, als ob die Anzahl an Leerzeichen nicht zu der Anzahl an Wörtern passt."
    assert all(
        isinstance(s, bool) for s in spaces
    ), "Die Leerzeichen-Angaben müssen boolesche Werte sein."
    assert [int(s) for s in spaces] == [0, 1, 1, 0, 0], "Sind die Leerzeichen korrekt?"
    assert (
        doc.text == "Na, alles klar?"
    ), "Bist du dir sicher, dass du das Doc richtig erstellt hast?"
    __msg__.good("Sehr schön!")
