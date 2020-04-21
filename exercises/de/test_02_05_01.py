def test():
    assert (
        "from spacy.tokens import Doc" in __solution__
    ), "Importierst du die Klasse Doc?"
    assert (
        doc.text == "spaCy ist cool!"
    ), "Bist du dir sicher, dass du das Doc richtig erstellt hast?"
    assert "print(doc.text)" in __solution__, "Druckst du den Text des Docs?"
    __msg__.good("Super!")
