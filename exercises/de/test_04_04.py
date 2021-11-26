def test():
    assert (
        'spacy.blank("de")' in __solution__
    ), "Nutzt du auch das deutsche Modell?"
    assert (
        "DocBin(docs=docs)" in __solution__
    ), "Hast du das DocBin-Objekt korrekt erstellt?"
    assert "doc_bin.to_disk(" in __solution__, "Nutzt du die Funktion to_disk?"
    assert "train.spacy" in __solution__, "Bist du sicher, dass du die Datei korrekt benannt hast?"

    __msg__.good(
        "Sehr gut! Nun können wir das Modell trainieren."
    )