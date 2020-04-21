def test():
    assert (
        "from spacy.tokens import Doc" in __solution__
    ), "Importierst du die Klasse Doc?"
    assert (
        len(words) == 5
    ), "Es sieht so aus, als ob du eine falsche Anzahl an Wörtern erstellt hast."
    assert (
        len(spaces) == 5
    ), "Es sieht so aus, als ob du eine falsche Anzahl an Leerzeichen erstellt hast."
    assert words == ["Was", ",", "echt", "?", "!"], "Schau dir nochmal die Wörter an!"
    assert all(
        isinstance(s, bool) for s in spaces
    ), "Die Leerzeichen-Werte müssen boolesche Werte sein."
    assert [int(s) for s in spaces] == [0, 1, 0, 0, 0], "Sind die Leerzeichen korrekt?"
    assert (
        doc.text == "Was, echt?!"
    ), "Bist du dir sicher, dass du das Doc richtig erstellt hast?"
    __msg__.good("Gut gemacht! Lass uns als nächstes ein paar Entitäten erstellen.")
