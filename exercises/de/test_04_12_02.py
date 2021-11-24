def test():
    assert (
        len(doc1.ents) == 2 and len(doc2.ents) == 2 and len(doc3.ents) == 2
    ), "Für alle Beispiele werden zwei Entitäten erwartet."
    assert any(
        e.label_ == "PER" and e.text == "PewDiePie" for e in doc2.ents
    ), "Hast du das Label PER korrekt zugeordnet?"
    assert any(
        e.label_ == "PER" and e.text == "Alexis Ohanian" for e in doc3.ents
    ), "Hast du das Label PER korrekt zugeordnet?"

    __msg__.good(
        "Bravo! Nachdem wir sowohl Beispiele der neuen WEBSITE-Entitäten, "
        "als auch vorhandene Entitäten wie PERSON in unsere Daten "
        "mitaufgenommen haben, erzielt das Modell nun deutlich bessere Ergebnisse."
    )
